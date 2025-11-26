from apolo_kube_client import (
    KubeClient,
    V1Container,
    V1LabelSelector,
    V1ObjectMeta,
    V1PodSpec,
    V1PodTemplateSpec,
    V1StatefulSet,
    V1StatefulSetSpec,
)


class TestStatefulSet:
    async def test_crud(self, kube_client: KubeClient) -> None:
        statefulset = V1StatefulSet(
            metadata=V1ObjectMeta(
                name="hello-world-statefulset", labels={"app": "hello-world"}
            ),
            spec=V1StatefulSetSpec(
                service_name="hello-world-service",
                replicas=1,
                selector=V1LabelSelector(match_labels={"app": "hello-world"}),
                template=V1PodTemplateSpec(
                    metadata=V1ObjectMeta(labels={"app": "hello-world"}),
                    spec=V1PodSpec(
                        containers=[
                            V1Container(name="hello-world", image="hello-world")
                        ]
                    ),
                ),
            ),
        )

        # test creating the statefulset
        statefulset_create = await kube_client.apps_v1.statefulset.create(
            model=statefulset, namespace="default"
        )
        assert statefulset_create.metadata.name == statefulset.metadata.name
        assert statefulset.metadata.name is not None

        # test getting the statefulset
        statefulset_get = await kube_client.apps_v1.statefulset.get(
            name=statefulset.metadata.name
        )
        assert statefulset_get.metadata.name == statefulset.metadata.name

        # test getting all statefulsets and ensuring the newly created statefulset is there
        statefulset_list = await kube_client.apps_v1.statefulset.get_list()
        statefulset_names = {p.metadata.name for p in statefulset_list.items}
        assert len(statefulset_list.items) > 0
        assert statefulset.metadata.name in statefulset_names

        # test deleting the statefulset
        ss_status = await kube_client.apps_v1.statefulset.delete(
            name=statefulset.metadata.name
        )
        assert ss_status.status == "Success"
