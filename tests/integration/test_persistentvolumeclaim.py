from apolo_kube_client import KubeClient
from apolo_kube_client import (
    V1ObjectMeta,
    V1PersistentVolumeClaim,
    V1PersistentVolumeClaimSpec,
    V1VolumeResourceRequirements,
)


class TestPersistentVolumeClaim:
    async def test_crud(self, kube_client: KubeClient) -> None:
        pvc = V1PersistentVolumeClaim(
            metadata=V1ObjectMeta(name="pvc-test", namespace="default"),
            spec=V1PersistentVolumeClaimSpec(
                access_modes=["ReadWriteOnce"],
                resources=V1VolumeResourceRequirements(requests={"storage": "1Gi"}),
                volume_mode="Filesystem",
            ),
        )

        # test creating the pvc
        pvc_create = await kube_client.core_v1.persistent_volume_claim.create(
            model=pvc, namespace="default"
        )
        assert pvc_create.metadata.name == pvc.metadata.name
        assert pvc.metadata.name is not None

        # test getting the pvc
        pvc_get = await kube_client.core_v1.persistent_volume_claim.get(
            name=pvc.metadata.name
        )
        assert pvc_get.metadata.name == pvc.metadata.name

        # test getting all pvcs and ensuring the newly created pvc is there
        pvc_list = await kube_client.core_v1.persistent_volume_claim.get_list()
        pvc_names = {p.metadata.name for p in pvc_list.items}
        assert len(pvc_list.items) > 0
        assert pvc.metadata.name in pvc_names

        # test deleting the pvc
        await kube_client.core_v1.persistent_volume_claim.delete(name=pvc.metadata.name)
