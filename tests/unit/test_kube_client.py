from collections.abc import AsyncIterator
from pathlib import Path
from unittest.mock import AsyncMock

import aiohttp
import pytest
from kubernetes.client import V1Namespace
from yarl import URL

from apolo_kube_client import KubeClient, KubeClientAuthType, KubeConfig
from apolo_kube_client._batch_v1 import BatchV1Api, Job
from apolo_kube_client._core import _KubeCore
from apolo_kube_client._core_v1 import CoreV1Api, Namespace
from apolo_kube_client._networking_k8s_io_v1 import NetworkingK8SioV1Api, NetworkPolicy
from apolo_kube_client._typedefs import NestedStrKeyDict
from apolo_kube_client._utils import generate_certs


@pytest.fixture
def kube_config_cert_auth(tmp_path: Path) -> KubeConfig:
    _, ca_cert = generate_certs("k8s-test-ca")
    auth_key, auth_cert = generate_certs("k8s-test-user")
    auth_cert_path = tmp_path / "auth_cert.pem"
    auth_cert_path.write_text(auth_cert)
    auth_cert_key_path = tmp_path / "auth_key.pem"
    auth_cert_key_path.write_text(auth_key)

    return KubeConfig(
        endpoint_url="https://k8s-test.com",
        cert_authority_data_pem=ca_cert,
        auth_cert_path=str(auth_cert_path),
        auth_cert_key_path=str(auth_cert_key_path),
        auth_type=KubeClientAuthType.CERTIFICATE,
        namespace="default",
    )


@pytest.fixture
def kube_config_token_auth() -> KubeConfig:
    return KubeConfig(
        endpoint_url="https://k8s-test.com",
        auth_type=KubeClientAuthType.TOKEN,
        token="token",
        namespace="default",
    )


@pytest.fixture
async def kube_client(kube_config_cert_auth: KubeConfig) -> AsyncIterator[KubeClient]:
    async with KubeClient(config=kube_config_cert_auth) as kube_client:
        yield kube_client


async def test_create_kube_client(kube_client: KubeClient) -> None:
    assert isinstance(kube_client, KubeClient)
    assert isinstance(kube_client._core, _KubeCore)
    assert kube_client._core.base_url == URL("https://k8s-test.com")
    assert kube_client._core._auth_type == KubeClientAuthType.CERTIFICATE
    assert kube_client._core._cert_authority_data_pem
    assert kube_client._core._auth_cert_path
    assert kube_client._core._auth_cert_key_path
    assert kube_client._core.namespace == "default"

    assert isinstance(kube_client.core_v1, CoreV1Api)
    assert isinstance(kube_client.batch_v1, BatchV1Api)
    assert isinstance(kube_client.networking_k8s_io_v1, NetworkingK8SioV1Api)

    assert isinstance(kube_client.core_v1.namespace, Namespace)
    assert isinstance(kube_client.batch_v1.job, Job)
    assert isinstance(kube_client.networking_k8s_io_v1.network_policy, NetworkPolicy)


async def test_create_kube_client_token_auth(
    kube_config_token_auth: KubeConfig,
) -> None:
    async with KubeClient(config=kube_config_token_auth) as kube_client:
        assert isinstance(kube_client, KubeClient)
        assert isinstance(kube_client._core, _KubeCore)
        assert kube_client._core.base_url == URL("https://k8s-test.com")
        assert kube_client._core._auth_type == KubeClientAuthType.TOKEN
        assert kube_client._core._token == "token"
        assert kube_client._core.namespace == "default"


async def test_deserialize_kube_client(kube_client: KubeClient) -> None:
    # test deserialization of a core_v1.namespace
    mock_resp = AsyncMock(spec=aiohttp.ClientResponse)
    mock_resp.status = 200
    mock_resp.reason = "OK"
    mock_resp.read.return_value = (
        b'{"kind":"Namespace","apiVersion":"v1","metadata":{"name":"test-ns"}}'
    )
    namespace = await kube_client.core_v1.namespace._deserialize(mock_resp, V1Namespace)
    assert isinstance(namespace, V1Namespace)
    assert namespace.metadata.name == "test-ns"

    # test dict to model deserialization
    resource_dict: NestedStrKeyDict = {
        "kind": "Namespace",
        "apiVersion": "v1",
        "metadata": {"name": "test-ns"},
    }

    namespace = kube_client.resource_dict_to_model(resource_dict, V1Namespace)
    assert isinstance(namespace, V1Namespace)
    assert namespace.metadata.name == "test-ns"


async def test_kube_client_build_post_json(kube_client: KubeClient) -> None:
    namespace = V1Namespace(
        api_version="v1", kind="Namespace", metadata={"name": "test-ns"}
    )
    post_json = kube_client.core_v1.namespace._build_post_json(namespace)
    assert post_json.keys() == {"apiVersion", "kind", "metadata"}  # type: ignore


async def test_escape_json_pointer(kube_client: KubeClient) -> None:
    # Test escaping of JSON pointers
    pointer = "/metadata/annotations~"
    escaped_pointer = kube_client.escape_json_pointer(pointer)
    assert escaped_pointer == "~1metadata~1annotations~0"
