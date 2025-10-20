from collections.abc import AsyncGenerator, Callable
from uuid import uuid4

import pytest

from apolo_kube_client import KubeClient
from apolo_kube_client._utils import base64_encode
from apolo_kube_client.models import (
    V1ObjectMeta,
    V1Secret,
)


@pytest.fixture
def secret_model_factory() -> Callable[[str, dict[str, str] | None], V1Secret]:
    def _create_secret_model(name: str, data: dict[str, str] | None = None) -> V1Secret:
        data = data or {}
        return V1Secret(
            api_version="v1",
            kind="Secret",
            metadata=V1ObjectMeta(name=name, namespace="default"),
            data={key: base64_encode(value) for key, value in data.items()},
            type="Opaque",
        )

    return _create_secret_model


@pytest.fixture
async def secret(
    kube_client: KubeClient,
    secret_model_factory: Callable[[str, dict[str, str] | None], V1Secret],
) -> AsyncGenerator[V1Secret]:
    secret = secret_model_factory(f"test-secret-{uuid4().hex[:8]}", {"key": "value"})
    yield await kube_client.core_v1.secret.create(model=secret, namespace="default")
    assert secret.metadata.name
    await kube_client.core_v1.secret.delete(
        name=secret.metadata.name, namespace="default"
    )


class TestSecret:
    async def test_crud(
        self,
        secret_model_factory: Callable[[str, dict[str, str] | None], V1Secret],
        kube_client: KubeClient,
    ) -> None:
        secret = secret_model_factory("secret", {"key": "value"})

        # test creating the secret
        secret_create = await kube_client.core_v1.secret.create(
            model=secret, namespace="default"
        )
        assert secret_create.metadata.name == secret.metadata.name
        assert secret.metadata.name

        # test getting the secret
        secret_get = await kube_client.core_v1.secret.get(name=secret.metadata.name)
        assert secret_get.metadata.name == secret.metadata.name

        # test getting all secres and ensuring the newly created secret is there
        secret_list = await kube_client.core_v1.secret.get_list()
        secret_names = {p.metadata.name for p in secret_list.items}
        assert len(secret_list.items) > 0
        assert secret.metadata.name in secret_names

        # test deleting the secret
        await kube_client.core_v1.secret.delete(name=secret.metadata.name)

    async def test_add_remove_keys(
        self,
        secret: V1Secret,
        kube_client: KubeClient,
    ) -> None:
        assert secret.metadata.name
        secret_with_new_key = await kube_client.core_v1.secret.add_key(
            name=secret.metadata.name,
            key="password",
            value="password",
            namespace="default",
        )

        assert secret_with_new_key.data["password"] == base64_encode("password")

        secret_without_new_key = await kube_client.core_v1.secret.delete_key(
            name=secret.metadata.name,
            key="password",
            namespace="default",
        )
        assert secret_without_new_key.data.get("password") is None
