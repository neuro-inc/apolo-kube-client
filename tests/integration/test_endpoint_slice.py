from apolo_kube_client import KubeClient


class TestEndpointSlice:
    async def test_get_list(self, kube_client: KubeClient) -> None:
        eps_list = await kube_client.discovery_k8s_io_v1.endpoint_slice.get_list(
            namespace="default"
        )
        assert len(eps_list.items) > 0

    async def test_get(self, kube_client: KubeClient) -> None:
        eps = await kube_client.discovery_k8s_io_v1.endpoint_slice.get(
            name="kubernetes", namespace="default"
        )
        assert eps
