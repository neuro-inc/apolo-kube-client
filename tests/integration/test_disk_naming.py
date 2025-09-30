from apolo_kube_client import KubeClient
from apolo_kube_client._crd_models import (
    V1DiskNamingCRD,
    V1DiskNamingCRDMetadata,
    V1DiskNamingCRDSpec,
)


class TestDiskNaming:
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
        dn_create = await kube_client.neuromation_io_v1.disk_naming.create(model=dn)
        assert dn_create.metadata.name == dn.metadata.name

        # test getting the dn
        dn_get = await kube_client.neuromation_io_v1.disk_naming.get(
            name=dn.metadata.name
        )
        assert dn_get.metadata.name == dn.metadata.name

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
