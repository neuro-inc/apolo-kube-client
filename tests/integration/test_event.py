import asyncio

from apolo_kube_client import KubeClient
from apolo_kube_client.models import (
    V1Container,
    V1ObjectMeta,
    V1Pod,
    V1PodSpec,
)


class TestEvent:
    async def test_events(self, kube_client: KubeClient) -> None:
        events = await kube_client.core_v1.event.get_list(
            namespace="default",
        )
        assert len(events.items) > 0

        # create a pod
        pod = V1Pod(
            api_version="v1",
            kind="Pod",
            metadata=V1ObjectMeta(name="test-pod"),
            spec=V1PodSpec(
                containers=[V1Container(name="hello-world", image="hello-world")],
                restart_policy="Never",
            ),
        )
        await kube_client.core_v1.pod.create(model=pod, namespace="default")

        # wait a bit until events will appear
        await asyncio.sleep(5)

        # get pod-related events
        pod_events = await kube_client.core_v1.event.get_list(
            field_selector=(
                "involvedObject.kind=Pod"
                f",involvedObject.namespace=default"
                f",involvedObject.name={pod.metadata.name}"
            )
        )
        assert len(pod_events.items) > 0

        for event in pod_events.items:
            assert event.involved_object.name == pod.metadata.name

        # delete a pod
        assert pod.metadata.name is not None
        await kube_client.core_v1.pod.delete(name=pod.metadata.name)
