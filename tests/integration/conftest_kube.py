import json
import subprocess
from collections.abc import AsyncIterator
from pathlib import Path
from typing import TypedDict, cast

import pytest

from apolo_kube_client import KubeClient, KubeClientAuthType, KubeConfig
from apolo_kube_client._typedefs import NestedStrKeyDict


# TODO: add analogue kubectl wait for the resource to be ready

KubeClusterPayload = TypedDict(
    "KubeClusterPayload", {"server": str, "certificate-authority": str}
)

KubeUserPayload = TypedDict(
    "KubeUserPayload", {"client-certificate": str, "client-key": str}
)


class KubeConfigPayload(TypedDict):
    clusters: list[NestedStrKeyDict]
    users: list[NestedStrKeyDict]
    contexts: list[NestedStrKeyDict]
    current_context: str


@pytest.fixture(scope="session")
def kube_config_payload() -> KubeConfigPayload:
    result = subprocess.run(
        ["kubectl", "config", "view", "-o", "json"], stdout=subprocess.PIPE
    )
    payload_str = result.stdout.decode().rstrip()
    return cast(KubeConfigPayload, json.loads(payload_str))


@pytest.fixture(scope="session")
def kube_config_cluster_payload(
    kube_config_payload: KubeConfigPayload,
) -> KubeClusterPayload:
    cluster_name = "minikube"
    clusters = {
        cluster["name"]: cluster["cluster"]
        for cluster in kube_config_payload["clusters"]
    }
    return cast(KubeClusterPayload, clusters[cluster_name])


@pytest.fixture(scope="session")
def kube_config_user_payload(
    kube_config_payload: KubeConfigPayload,
) -> KubeUserPayload:
    user_name = "minikube"
    users = {user["name"]: user["user"] for user in kube_config_payload["users"]}
    return cast(KubeUserPayload, users[user_name])


@pytest.fixture(scope="session")
def cert_authority_data_pem(
    kube_config_cluster_payload: KubeClusterPayload,
) -> str | None:
    ca_path = kube_config_cluster_payload["certificate-authority"]
    if ca_path:
        return Path(ca_path).read_text()
    return None


@pytest.fixture
async def kube_config(
    kube_config_cluster_payload: KubeClusterPayload,
    kube_config_user_payload: KubeUserPayload,
    cert_authority_data_pem: str | None,
) -> KubeConfig:
    cluster = kube_config_cluster_payload
    user = kube_config_user_payload
    return KubeConfig(
        endpoint_url=cluster["server"],
        cert_authority_data_pem=cert_authority_data_pem,
        auth_cert_path=user["client-certificate"],
        auth_cert_key_path=user["client-key"],
        auth_type=KubeClientAuthType.CERTIFICATE,
    )


@pytest.fixture
async def kube_client(kube_config: KubeConfig) -> AsyncIterator[KubeClient]:
    async with KubeClient(config=kube_config) as client:
        yield client
