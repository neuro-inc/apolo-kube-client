from kubernetes.client import V1ObjectMeta, V1StorageClass

from apolo_kube_client import KubeClient


class TestStorageClass:
    async def test_crud(self, kube_client: KubeClient) -> None:
        storage_class = V1StorageClass(
            api_version="storage.k8s.io/v1",
            kind="StorageClass",
            metadata=V1ObjectMeta(name="test-storage-class"),
            provisioner="kubernetes.io/no-provisioner",
            reclaim_policy="Delete",
            volume_binding_mode="WaitForFirstConsumer",
        )

        # test creating the storage_class
        storage_class_create = await kube_client.storage_k8s_io_v1.storage_class.create(
            model=storage_class
        )
        assert storage_class_create.metadata.name == storage_class.metadata.name

        # test getting the storage_class
        storage_class_get = await kube_client.storage_k8s_io_v1.storage_class.get(
            name=storage_class.metadata.name
        )
        assert storage_class_get.metadata.name == storage_class.metadata.name

        # test getting all storage_classs and ensuring the newly created storage_class is there
        storage_class_list = (
            await kube_client.storage_k8s_io_v1.storage_class.get_list()
        )
        storage_class_names = {s.metadata.name for s in storage_class_list.items}
        assert len(storage_class_list.items) > 0
        assert storage_class.metadata.name in storage_class_names

        # test deleting the storage_class
        await kube_client.storage_k8s_io_v1.storage_class.delete(
            name=storage_class.metadata.name
        )
