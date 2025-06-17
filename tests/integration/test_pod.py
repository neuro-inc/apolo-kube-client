from kubernetes.client import (
    V1Container,
    V1ObjectMeta,
    V1Pod,
    V1PodSpec,
)

from apolo_kube_client import KubeClient


class TestPod:
    async def test_crud(self, kube_client: KubeClient) -> None:
        pod = V1Pod(
            api_version="v1",
            kind="Pod",
            metadata=V1ObjectMeta(name="test-hello-world-pod"),
            spec=V1PodSpec(
                containers=[V1Container(name="hello-world", image="hello-world")],
                restart_policy="Never",
            ),
        )

        # test creating the pod
        pod_create = await kube_client.core_v1.pod.create(
            model=pod, namespace="default"
        )
        assert pod_create.metadata.name == pod.metadata.name

        # test getting the pod
        pod_get = await kube_client.core_v1.pod.get(name=pod.metadata.name)
        assert pod_get.metadata.name == pod.metadata.name

        # test getting all pods and ensuring the newly created pod is there
        pod_list = await kube_client.core_v1.pod.get_list()
        pod_names = {p.metadata.name for p in pod_list.items}
        assert len(pod_list.items) > 0
        assert pod.metadata.name in pod_names

        # test deleting the pod
        await kube_client.core_v1.pod.delete(name=pod.metadata.name)
