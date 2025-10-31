from apolo_kube_client import KubeClient


class TestNode:
    async def test_get(self, kube_client: KubeClient) -> None:
        # test getting all nodes
        node_list = await kube_client.core_v1.node.get_list()
        assert len(node_list.items) > 0
        assert node_list.items[0].metadata.name is not None

        # test getting the node by name
        await kube_client.core_v1.node.get(name=node_list.items[0].metadata.name)

        # test proxy stats summary
        stats_res = await kube_client.core_v1.node.get_stats_summary(
            name=node_list.items[0].metadata.name
        )
        assert len(stats_res.pods) >= 0
