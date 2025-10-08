from apolo_kube_client import KubeClient


class TestNode:
    async def test_get(self, kube_client: KubeClient) -> None:
        # test getting all nodes
        node_list = await kube_client.core_v1.node.get_list()
        assert len(node_list.items) > 0

        # test getting the node by name
        await kube_client.core_v1.node.get(name=node_list.items[0].metadata.name)

        # test proxy stats summary
        stats_res = await kube_client.core_v1.node.get_stats_summary(
            name=node_list.items[0].metadata.name
        )
        assert stats_res["node"]  # type: ignore
        assert stats_res["pods"]  # type: ignore
