import asyncio
from collections.abc import AsyncGenerator

import pytest

from apolo_kube_client import KubeClient
from apolo_kube_client._crd_models import (
    V1DiskNamingCRD,
    V1DiskNamingCRDMetadata,
    V1DiskNamingCRDSpec,
)
from apolo_kube_client import (
    V1CustomResourceColumnDefinition,
    V1CustomResourceDefinition,
    V1CustomResourceDefinitionNames,
    V1CustomResourceDefinitionSpec,
    V1CustomResourceDefinitionVersion,
    V1CustomResourceValidation,
    V1JSONSchemaProps,
    V1ObjectMeta,
)


@pytest.fixture
async def install_disk_naming_crd(kube_client: KubeClient) -> AsyncGenerator[None]:
    dn_crd = V1CustomResourceDefinition(
        metadata=V1ObjectMeta(name="disknamings.neuromation.io"),
        spec=V1CustomResourceDefinitionSpec(
            group="neuromation.io",
            versions=[
                V1CustomResourceDefinitionVersion(
                    name="v1",
                    served=True,
                    storage=True,
                    schema_=V1CustomResourceValidation(
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

    await kube_client.extensions_k8s_io_v1.crd.create(model=dn_crd)
    await asyncio.sleep(1)
    yield
    assert dn_crd.metadata.name is not None
    await kube_client.extensions_k8s_io_v1.crd.delete(name=dn_crd.metadata.name)


class TestDiskNaming:
    @pytest.mark.usefixtures("install_disk_naming_crd")
    async def test_crud(self, kube_client: KubeClient) -> None:
        dn = V1DiskNamingCRD(
            apiVersion="neuromation.io/v1",
            kind="DiskNaming",
            metadata=V1DiskNamingCRDMetadata(
                name="disknaming-test", namespace="default"
            ),
            spec=V1DiskNamingCRDSpec(disk_id="disk-12345"),
        )

        # test creating the dn
        (
            created,
            dn_create,
        ) = await kube_client.neuromation_io_v1.disk_naming.create_or_update(model=dn)
        assert dn_create.metadata.name == dn.metadata.name

        # test getting the dn
        dn_get = await kube_client.neuromation_io_v1.disk_naming.get(
            name=dn.metadata.name
        )
        assert dn_get.metadata.name == dn.metadata.name

        # test update the dn
        dn_get.spec.disk_id = "disk-67890"
        dn_update = await kube_client.neuromation_io_v1.disk_naming.update(model=dn_get)
        assert dn_update.spec.disk_id == "disk-67890"

        # test getting all dns and ensuring the newly created dn is there
        dn_list = await kube_client.neuromation_io_v1.disk_naming.get_list()
        dn_names = {d.metadata.name for d in dn_list.items}
        assert len(dn_list.items) > 0
        assert dn.metadata.name in dn_names

        # test deleting the dn
        dn_status = await kube_client.neuromation_io_v1.disk_naming.delete(
            name=dn.metadata.name
        )
        assert dn_status.status == "Success"
