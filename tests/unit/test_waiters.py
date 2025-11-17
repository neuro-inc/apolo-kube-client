import pytest

from apolo_kube_client import (
    ResourceNotFound,
    V1ContainerState,
    V1ContainerStateRunning,
    V1ContainerStateWaiting,
    V1ContainerStateTerminated,
    V1ContainerStatus,
    V1ObjectMeta,
    V1Pod,
    V1PodStatus,
)
from apolo_kube_client._apolo_waiters import ApoloPodWaiter


def _pod_with_phase(phase: str) -> V1Pod:
    return V1Pod(metadata=V1ObjectMeta(name="p"), status=V1PodStatus(phase=phase))


def _pod_with_waiting(reason: str | None) -> V1Pod:
    if reason is not None:
        state = V1ContainerState(waiting=V1ContainerStateWaiting(reason=reason))
    else:
        state = V1ContainerState(running=V1ContainerStateRunning())
    cs = V1ContainerStatus(
        name="c",
        image="busybox",
        image_id="busybox@sha256:dummy",
        ready=False,
        restart_count=0,
        state=state,
    )
    return V1Pod(
        metadata=V1ObjectMeta(name="p"),
        status=V1PodStatus(container_statuses=[cs]),
    )


def _pod_with_terminated() -> V1Pod:
    state = V1ContainerState(terminated=V1ContainerStateTerminated(exit_code=0))
    cs = V1ContainerStatus(
        name="c",
        image="busybox",
        image_id="busybox@sha256:dummy",
        ready=False,
        restart_count=0,
        state=state,
    )
    return V1Pod(
        metadata=V1ObjectMeta(name="p"),
        status=V1PodStatus(container_statuses=[cs]),
    )


class _StubParent:
    """Minimal parent stub for NestedResource to test ApoloPodWaiter."""

    def __init__(self, responses: list[V1Pod | Exception]):
        self._responses = iter(responses)
        self._core = object()  # not used by waiters
        self._group_api_query_path = "api/v1"
        self._resource_id = "p"

    async def get(self, name: str, namespace: str | None = None) -> V1Pod:
        try:
            nxt = next(self._responses)
        except StopIteration:  # pragma: no cover
            nxt = _pod_with_phase("Running")
        if isinstance(nxt, Exception):
            raise nxt
        return nxt


@pytest.mark.asyncio
async def test_apolo_waiter_wait_finished() -> None:
    parent = _StubParent(
        [
            _pod_with_phase("Pending"),
            _pod_with_phase("Succeeded"),
        ]
    )
    waiter = ApoloPodWaiter(parent)  # type: ignore[arg-type]
    pod = await waiter.wait_finished(timeout_s=1.0, interval_s=0.01)
    assert pod.status.phase == "Succeeded"


@pytest.mark.asyncio
async def test_apolo_waiter_wait_deleted() -> None:
    parent = _StubParent(
        [
            _pod_with_phase("Running"),
            ResourceNotFound("missing"),
        ]
    )
    waiter = ApoloPodWaiter(parent)  # type: ignore[arg-type]
    await waiter.wait_deleted(timeout_s=1.0, interval_s=0.01)


@pytest.mark.asyncio
async def test_apolo_waiter_wait_not_waiting() -> None:
    parent = _StubParent(
        [
            _pod_with_waiting("ContainerCreating"),
            _pod_with_waiting(None),
        ]
    )
    waiter = ApoloPodWaiter(parent)  # type: ignore[arg-type]
    pod = await waiter.wait_not_waiting(timeout_s=1.0, interval_s=0.01)
    assert not pod.status.container_statuses[0].state.waiting.__pydantic_fields_set__


@pytest.mark.asyncio
async def test_apolo_waiter_wait_running() -> None:
    parent = _StubParent(
        [
            _pod_with_phase("Pending"),
            _pod_with_phase("Running"),
        ]
    )
    waiter = ApoloPodWaiter(parent)  # type: ignore[arg-type]
    pod = await waiter.wait_running(timeout_s=1.0, interval_s=0.01)
    assert pod.status.phase == "Running"


@pytest.mark.asyncio
async def test_apolo_waiter_wait_terminated_all_containers() -> None:
    parent = _StubParent(
        [
            _pod_with_phase("Running"),
            _pod_with_terminated(),
        ]
    )
    waiter = ApoloPodWaiter(parent)  # type: ignore[arg-type]
    pod = await waiter.wait_terminated(timeout_s=1.0, interval_s=0.01)
    assert pod is not None
    assert pod.status.container_statuses[0].state.terminated is not None


@pytest.mark.asyncio
async def test_apolo_waiter_wait_terminated_allow_not_exists_true() -> None:
    parent = _StubParent(
        [
            ResourceNotFound("missing"),
        ]
    )
    waiter = ApoloPodWaiter(parent)  # type: ignore[arg-type]
    pod = await waiter.wait_terminated(
        timeout_s=1.0,
        interval_s=0.01,
        allow_pod_not_exists=True,
    )
    assert pod is None


@pytest.mark.asyncio
async def test_apolo_waiter_wait_terminated_allow_not_exists_false() -> None:
    parent = _StubParent(
        [
            ResourceNotFound("missing"),
        ]
    )
    waiter = ApoloPodWaiter(parent)  # type: ignore[arg-type]
    with pytest.raises(ResourceNotFound):
        await waiter.wait_terminated(
            timeout_s=1.0,
            interval_s=0.01,
            allow_pod_not_exists=False,
        )
