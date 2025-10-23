from apolo_kube_client import KubeClient
from apolo_kube_client import (
    V1ObjectMeta,
    V1PersistentVolume,
    V1PersistentVolumeSpec,
    V1HostPathVolumeSource,
)


class TestPersistentVolume:
    async def test_crud(self, kube_client: KubeClient) -> None:
        pv = V1PersistentVolume(
            api_version="v1",
            kind="PersistentVolume",
            metadata=V1ObjectMeta(name="pvc-test"),
            spec=V1PersistentVolumeSpec(
                access_modes=["ReadWriteOnce"],
                capacity={"storage": "1Gi"},
                persistent_volume_reclaim_policy="Delete",
                storage_class_name="standard",
                volume_mode="Filesystem",
                host_path=V1HostPathVolumeSource(path="/tmp/data"),
            ),
        )

        # test creating the pv
        pv_create = await kube_client.core_v1.persistent_volume.create(model=pv)
        assert pv_create.metadata.name == pv.metadata.name
        assert pv.metadata.name is not None

        # test getting the pv
        pv_get = await kube_client.core_v1.persistent_volume.get(name=pv.metadata.name)
        assert pv_get.metadata.name == pv.metadata.name

        # test getting all pvs and ensuring the newly created pv is there
        pv_list = await kube_client.core_v1.persistent_volume.get_list()
        pv_names = {p.metadata.name for p in pv_list.items}
        assert len(pv_list.items) > 0
        assert pv.metadata.name in pv_names

        # test deleting the pv
        await kube_client.core_v1.persistent_volume.delete(name=pv.metadata.name)
