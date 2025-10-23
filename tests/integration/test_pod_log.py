import asyncio
import datetime as dt
import re
from uuid import uuid4

import pytest
from kubernetes.client import (
    V1Container,
    V1ObjectMeta,
    V1Pod,
    V1PodSpec,
)

from apolo_kube_client import KubeClient
from apolo_kube_client._errors import ResourceBadRequest


async def _wait_pod_succeeded(kube_client: KubeClient, name: str) -> V1Pod:
    while True:
        await asyncio.sleep(0.5)
        pod = await kube_client.core_v1.pod.get(name=name)
        if pod.status.phase == "Succeeded":
            return pod


class TestPodLog:
    async def test_read(self, kube_client: KubeClient) -> None:
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
        await _wait_pod_succeeded(kube_client, pod_name)

        logs = await kube_client.core_v1.pod[pod_name].log.read()
        assert "Hello from Docker!" in logs
        await kube_client.core_v1.pod.delete(name=pod_name)

    async def test_read_follow(self, kube_client: KubeClient) -> None:
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
        await _wait_pod_succeeded(kube_client, pod_name)

        logs = await kube_client.core_v1.pod[pod_name].log.read(follow=True)
        assert "Hello from Docker!" in logs
        await kube_client.core_v1.pod.delete(name=pod_name)

    async def test_read_timestamps(self, kube_client: KubeClient) -> None:
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
        await _wait_pod_succeeded(kube_client, pod_name)

        logs = await kube_client.core_v1.pod[pod_name].log.read(timestamps=True)
        # Expect ISO8601 prefix on each non-empty line
        lines = [ln for ln in logs.splitlines() if ln.strip()]
        assert lines, "expected at least one log line"
        ts_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:")
        assert all(ts_pattern.match(ln) for ln in lines)
        await kube_client.core_v1.pod.delete(name=pod_name)

    async def test_read_since_time(self, kube_client: KubeClient) -> None:
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
        await _wait_pod_succeeded(kube_client, pod_name)

        now_utc = dt.datetime.now(dt.timezone.utc)
        future = now_utc + dt.timedelta(minutes=10)
        past = now_utc - dt.timedelta(days=1)

        empty_logs = await kube_client.core_v1.pod[pod_name].log.read(since=future)
        assert empty_logs.strip() == ""

        logs = await kube_client.core_v1.pod[pod_name].log.read(since=past)
        assert "Hello from Docker!" in logs
        await kube_client.core_v1.pod.delete(name=pod_name)

    async def test_read_multi_container_requires_container(
        self, kube_client: KubeClient
    ) -> None:
        pod_name = uuid4().hex
        pod = V1Pod(
            api_version="v1",
            kind="Pod",
            metadata=V1ObjectMeta(name=pod_name),
            spec=V1PodSpec(
                containers=[
                    V1Container(name="c1", image="hello-world"),
                    V1Container(name="c2", image="hello-world"),
                ],
                restart_policy="Never",
            ),
        )
        await kube_client.core_v1.pod.create(pod)
        await _wait_pod_succeeded(kube_client, pod_name)

        # Without container name, API should return 400
        with pytest.raises(ResourceBadRequest):
            await kube_client.core_v1.pod[pod_name].log.read()

        logs_c1 = await kube_client.core_v1.pod[pod_name].log.read(container="c1")
        logs_c2 = await kube_client.core_v1.pod[pod_name].log.read(container="c2")
        assert "Hello from Docker!" in logs_c1
        assert "Hello from Docker!" in logs_c2
        await kube_client.core_v1.pod.delete(name=pod_name)

    async def test_read_previous_and_bad_container_errors(
        self, kube_client: KubeClient
    ) -> None:
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
        await _wait_pod_succeeded(kube_client, pod_name)

        # No previous container exists -> expect 400
        with pytest.raises(ResourceBadRequest):
            await kube_client.core_v1.pod[pod_name].log.read(previous=True)

        # Non-existent container name -> expect 400
        with pytest.raises(ResourceBadRequest):
            await kube_client.core_v1.pod[pod_name].log.read(container="nope")

        await kube_client.core_v1.pod.delete(name=pod_name)
