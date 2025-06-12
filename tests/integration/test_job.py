from kubernetes.client import (
    V1Container,
    V1Job,
    V1JobSpec,
    V1ObjectMeta,
    V1PodSpec,
    V1PodTemplateSpec,
)

from apolo_kube_client import KubeClient


class TestJob:
    async def test_crud(self, kube_client: KubeClient) -> None:
        job = V1Job(
            api_version="batch/v1",
            kind="Job",
            metadata=V1ObjectMeta(name="test-hello-world-job"),
            spec=V1JobSpec(
                template=V1PodTemplateSpec(
                    spec=V1PodSpec(
                        containers=[V1Container(name="hello", image="hello-world")],
                        restart_policy="Never",
                    )
                )
            ),
        )

        # test creating a network policy
        job_create = await kube_client.batch_v1.job.create(
            model=job, namespace="default"
        )
        assert job_create.metadata.name == job.metadata.name

        # test getting the network policy
        job_get = await kube_client.batch_v1.job.get(name=job.metadata.name)
        assert job_get.metadata.name == job.metadata.name

        # test listing network policies
        job_list = await kube_client.batch_v1.job.list()
        job_names = {j.metadata.name for j in job_list.items}
        assert len(job_list.items) > 0
        assert job.metadata.name in job_names

        # test deleting the network policy
        await kube_client.batch_v1.job.delete(name=job.metadata.name)
