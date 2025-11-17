import asyncio
from uuid import uuid4


from apolo_kube_client import KubeClient
from apolo_kube_client import V1Container, V1ObjectMeta, V1Pod, V1PodSpec
from apolo_kube_client._apolo_waiters import _PodStatus


class TestApoloPodWaiters:
    async def test_wait_finished_then_delete(self, kube_client: KubeClient) -> None:
        pod_name = f"waiter-finish-{uuid4().hex[:8]}"
        pod = V1Pod(
            metadata=V1ObjectMeta(name=pod_name),
            spec=V1PodSpec(
                containers=[V1Container(name="hello-world", image="hello-world")],
                restart_policy="Never",
            ),
        )
        await kube_client.core_v1.pod.create(pod)

        pod_done = await kube_client.core_v1.pod[pod_name].apolo_waiter.wait_finished(
            timeout_s=300, interval_s=1.0
        )
        assert pod_done.status.phase in {_PodStatus.SUCCEEDED, _PodStatus.FAILED}

        await kube_client.core_v1.pod.delete(name=pod_name)
        await kube_client.core_v1.pod[pod_name].apolo_waiter.wait_deleted(
            timeout_s=120, interval_s=1.0
        )

    async def test_wait_terminated(self, kube_client: KubeClient) -> None:
        pod_name = f"waiter-terminated-{uuid4().hex[:8]}"
        pod = V1Pod(
            metadata=V1ObjectMeta(name=pod_name),
            spec=V1PodSpec(
                containers=[
                    V1Container(
                        name="terminating",
                        image="busybox:1.36",
                        image_pull_policy="IfNotPresent",
                        command=["/bin/sh", "-c", "echo terminating && sleep 1"],
                    )
                ],
                restart_policy="Never",
            ),
        )
        await kube_client.core_v1.pod.create(pod)

        pod_terminated = await kube_client.core_v1.pod[
            pod_name
        ].apolo_waiter.wait_terminated(timeout_s=300, interval_s=1.0)
        assert pod_terminated
        assert len(pod_terminated.status.container_statuses) > 0
        for container in pod_terminated.status.container_statuses:
            assert container.state.terminated is not None

        # Cleanup; ignore errors during deletion in CI.
        try:
            await kube_client.core_v1.pod.delete(name=pod_name)
            await kube_client.core_v1.pod[pod_name].apolo_waiter.wait_deleted(
                timeout_s=120, interval_s=1.0
            )
        except Exception:
            pass

    async def test_wait_terminated_allow_pod_not_exists(
        self, kube_client: KubeClient
    ) -> None:
        # Use a random name and do not create the pod at all.
        # wait_terminated with allow_pod_not_exists=True should treat 404 as success.
        pod_name = f"waiter-terminated-missing-{uuid4().hex[:8]}"

        pod = await kube_client.core_v1.pod[pod_name].apolo_waiter.wait_terminated(
            timeout_s=60,
            interval_s=1.0,
            allow_pod_not_exists=True,
        )
        assert pod is None

    async def test_wait_running_and_deleted(self, kube_client: KubeClient) -> None:
        pod_name = f"waiter-running-{uuid4().hex[:8]}"
        pod = V1Pod(
            metadata=V1ObjectMeta(name=pod_name),
            spec=V1PodSpec(
                containers=[
                    V1Container(
                        name="sleeper",
                        image="busybox:1.36",
                        image_pull_policy="IfNotPresent",
                        command=["/bin/sh", "-c", "sleep 30"],
                    )
                ],
                restart_policy="Never",
            ),
        )
        await kube_client.core_v1.pod.create(pod)

        pod_running = await kube_client.core_v1.pod[pod_name].apolo_waiter.wait_running(
            timeout_s=300, interval_s=1.0
        )
        assert pod_running.status.phase == _PodStatus.RUNNING

        await kube_client.core_v1.pod.delete(name=pod_name)
        await kube_client.core_v1.pod[pod_name].apolo_waiter.wait_deleted(
            timeout_s=120, interval_s=1.0
        )

    async def test_wait_scheduled_and_not_waiting(
        self, kube_client: KubeClient
    ) -> None:
        pod_name = f"waiter-scheduled-{uuid4().hex[:8]}"
        pod = V1Pod(
            metadata=V1ObjectMeta(name=pod_name),
            spec=V1PodSpec(
                containers=[
                    V1Container(
                        name="quick",
                        image="busybox:1.36",
                        image_pull_policy="IfNotPresent",
                        command=["/bin/sh", "-c", "echo OK"],
                    )
                ],
                restart_policy="Never",
            ),
        )
        await kube_client.core_v1.pod.create(pod)

        pod_scheduled = await kube_client.core_v1.pod[
            pod_name
        ].apolo_waiter.wait_scheduled(timeout_s=300, interval_s=1.0)
        assert pod_scheduled.status.host_ip or pod_scheduled.status.conditions

        pod_not_waiting = await kube_client.core_v1.pod[
            pod_name
        ].apolo_waiter.wait_not_waiting(timeout_s=300, interval_s=1.0)
        # If the pod completed very quickly, it may already be Succeeded.
        assert pod_not_waiting.status.phase in {
            _PodStatus.PENDING,
            _PodStatus.RUNNING,
            _PodStatus.SUCCEEDED,
            _PodStatus.FAILED,
        }

        # Optionally, wait a bit for it to finish; ignore timeouts.
        try:
            await asyncio.wait_for(
                kube_client.core_v1.pod[pod_name].apolo_waiter.wait_finished(
                    timeout_s=10, interval_s=0.5
                ),
                timeout=15,
            )
        except Exception:
            pass
        # Delete regardless of state; ignore errors during cleanup in CI.
        try:
            await kube_client.core_v1.pod.delete(name=pod_name)
            await kube_client.core_v1.pod[pod_name].apolo_waiter.wait_deleted(
                timeout_s=120, interval_s=1.0
            )
        except Exception:
            pass
