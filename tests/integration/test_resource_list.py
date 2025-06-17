from apolo_kube_client import KubeClient
from apolo_kube_client._batch_v1 import BatchV1Api


class TestResourceList:
    async def test_get_resource_list(self, kube_client: KubeClient) -> None:
        # Test retrieving the resource list for BatchV1Api
        resource_list = await kube_client.resource_list.get_list(
            resource_list_path=BatchV1Api.group_api_query_path
        )
        resource_names = {r.kind for r in resource_list.resources}
        assert resource_names == {"Job", "CronJob"}

    async def test_find_resource_by_kind(self, kube_client: KubeClient) -> None:
        # Test finding a resource by kind
        resource = await kube_client.resource_list.find_resource_by_kind(
            kind="Job", resource_list_path=BatchV1Api.group_api_query_path
        )
        assert resource is not None
        assert resource.kind == "Job"
        assert resource.name == "jobs"
        assert resource.namespaced is True

        # Test with a non-existent kind
        non_existent_resource = await kube_client.resource_list.find_resource_by_kind(
            "NonExistentKind", BatchV1Api.group_api_query_path
        )
        assert non_existent_resource is None
