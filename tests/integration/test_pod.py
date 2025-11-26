from apolo_kube_client import (
    KubeClient,
    V1Container,
    V1ObjectMeta,
    V1Pod,
    V1PodSpec,
)


class TestPod:
    async def test_crud(self, kube_client: KubeClient) -> None:
        pod = V1Pod(
            metadata=V1ObjectMeta(
                name="test-hello-world-pod", labels={"app": "hello-world"}
            ),
            spec=V1PodSpec(
                containers=[V1Container(name="hello-world", image="hello-world")],
                restart_policy="Never",
            ),
        )

        # test getting all pods in all namespaces
        pod_list = await kube_client.core_v1.pod.get_list(all_namespaces=True)
        pod_namespaces = {p.metadata.namespace for p in pod_list.items}
        assert len(pod_list.items) > 0
        assert "kube-system" in pod_namespaces

        # test creating the pod
        pod_create = await kube_client.core_v1.pod.create(
            model=pod, namespace="default"
        )
        assert pod_create.metadata.name == pod.metadata.name
        assert pod.metadata.name is not None

        # test getting the pod
        pod_get = await kube_client.core_v1.pod.get(name=pod.metadata.name)
        assert pod_get.metadata.name == pod.metadata.name

        # test getting all pods and ensuring the newly created pod is there
        pod_list = await kube_client.core_v1.pod.get_list()
        pod_names = {p.metadata.name for p in pod_list.items}
        assert len(pod_list.items) > 0
        assert pod.metadata.name in pod_names

        # test getting pods with label selector
        pod_list_with_existing_label_selector = await kube_client.core_v1.pod.get_list(
            label_selector="app=hello-world"
        )
        assert len(pod_list_with_existing_label_selector.items) == 1
        pod_list_with_not_existing_label_selector = (
            await kube_client.core_v1.pod.get_list(label_selector="app=hello-world2")
        )
        assert len(pod_list_with_not_existing_label_selector.items) == 0

        # test deleting the pod
        await kube_client.core_v1.pod.delete(name=pod.metadata.name)
