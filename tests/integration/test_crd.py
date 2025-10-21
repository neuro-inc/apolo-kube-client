import asyncio
import time

import pytest
from kubernetes.client import (
    V1CustomResourceColumnDefinition,
    V1CustomResourceDefinition,
    V1CustomResourceDefinitionNames,
    V1CustomResourceDefinitionSpec,
    V1CustomResourceDefinitionVersion,
    V1CustomResourceValidation,
    V1JSONSchemaProps,
    V1ObjectMeta,
)

from apolo_kube_client import KubeClient, ResourceNotFound


@pytest.fixture
def crd() -> V1CustomResourceDefinition:
    return V1CustomResourceDefinition(
        api_version="apiextensions.k8s.io/v1",
        kind="CustomResourceDefinition",
        metadata=V1ObjectMeta(name="disknamings.neuromation.io"),
        spec=V1CustomResourceDefinitionSpec(
            group="neuromation.io",
            versions=[
                V1CustomResourceDefinitionVersion(
                    name="v1",
                    served=True,
                    storage=True,
                    schema=V1CustomResourceValidation(
                        open_apiv3_schema=V1JSONSchemaProps(
                            type="object",
                            properties={
                                "spec": V1JSONSchemaProps(
                                    type="object",
                                    properties={
                                        "disk_id": V1JSONSchemaProps(type="string")
                                    },
                                )
                            },
                        )
                    ),
                    additional_printer_columns=[
                        V1CustomResourceColumnDefinition(
                            name="DiskNaming", type="string", json_path=".spec.disk_id"
                        )
                    ],
                )
            ],
            scope="Namespaced",
            names=V1CustomResourceDefinitionNames(
                kind="DiskNaming",
                list_kind="DiskNamingsList",
                plural="disknamings",
                singular="disknaming",
                short_names=[],
            ),
        ),
    )


class TestCRD:
    async def test_crd_namespaced_crud(
        self, crd: V1CustomResourceDefinition, kube_client: KubeClient
    ) -> None:
        # test creating the crd
        (
            created,
            crd_create,
        ) = await kube_client.extensions_k8s_io_v1.crd.create_or_update(model=crd)
        assert crd_create.metadata.name == crd.metadata.name

        # test getting the crd
        crd_get = await kube_client.extensions_k8s_io_v1.crd.get(name=crd.metadata.name)
        assert crd_get.metadata.name == crd.metadata.name

        # test getting all crds and ensuring the newly created crd is there
        crd_list = await kube_client.extensions_k8s_io_v1.crd.get_list()
        crd_names = {c.metadata.name for c in crd_list.items}
        assert len(crd_list.items) > 0
        assert crd.metadata.name in crd_names

        # test deleting the crd
        await kube_client.extensions_k8s_io_v1.crd.delete(name=crd.metadata.name)

        with pytest.raises(ResourceNotFound):
            t0 = time.monotonic()
            delta = 0.1
            while time.monotonic() - t0 < 10.0:
                await kube_client.extensions_k8s_io_v1.crd.get(name=crd.metadata.name)
                await asyncio.sleep(min(delta, 1))
                delta *= 2
            raise TimeoutError
