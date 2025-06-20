from apolo_kube_client import KubeClient


class TestPod:
    async def test_get(self, kube_client: KubeClient) -> None:
        # test getting all pods and ensuring the newly created pod is there
        node_list = await kube_client.core_v1.node.get_list()
        assert len(node_list.items) > 0

        # test getting the pod
        await kube_client.core_v1.node.get(name=node_list.items[0].metadata.name)
