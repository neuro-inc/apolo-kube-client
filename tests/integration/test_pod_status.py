import asyncio
from uuid import uuid4

from apolo_kube_client import (
    V1Container,
    V1ObjectMeta,
    V1Pod,
    V1PodSpec,
    V1PodStatus,
)

from apolo_kube_client import KubeClient


class TestPodStatus:
    async def test_crud(self, kube_client: KubeClient) -> None:
        pod_name = uuid4().hex

        pod = V1Pod(
            api_version="v1",
            kind="Pod",
            metadata=V1ObjectMeta(name=pod_name),
            spec=V1PodSpec(
                containers=[V1Container(name="hello-world", image="hello-world")],
                restart_policy="Never",
            ),
        )

        await kube_client.core_v1.pod.create(pod)

        # let's update the status
        pod.status = V1PodStatus(reason="Custom")
        await kube_client.core_v1.pod[pod_name].status.update(pod)

        # re-fetch
        for attempt in range(100):
            pod = await kube_client.core_v1.pod.get(name=pod_name)
            if pod.status.reason is None:
                await asyncio.sleep(0.01)
                continue
            assert pod.status.reason == "Custom"
            break
        else:
            raise AssertionError("Waiting for status update has failed")

        await kube_client.core_v1.pod.delete(name=pod_name)
