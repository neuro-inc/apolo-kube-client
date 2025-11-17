import asyncio
from enum import StrEnum
from typing import Awaitable, Callable

from ._base_resource import NestedResource
from ._errors import KubeClientException, ResourceGone, ResourceNotFound
from ._models import V1Pod


class _PodStatus(StrEnum):
    PENDING = "Pending"
    RUNNING = "Running"
    SUCCEEDED = "Succeeded"
    FAILED = "Failed"


class ApoloPodWaiter(NestedResource[V1Pod]):
    """Synthetic nested resource that provides pod waiters utilities.

    Usage:
    >>> await client.core_v1.pod["pod-name"].apolo_waiter.wait_finished()
    """

    query_path = "apolo-waiter"  # logical name. no direct HTTP usage

    async def wait_running(
        self,
        *,
        timeout_s: float = 10.0 * 60,
        interval_s: float = 1.0,
    ) -> V1Pod:
        async def _is_running(pod: V1Pod) -> bool:
            return (pod.status.phase or "") == _PodStatus.RUNNING

        return await self._wait_via_getter(
            is_satisfied=_is_running,
            timeout_s=timeout_s,
            interval_s=interval_s,
        )

    async def wait_finished(
        self,
        *,
        timeout_s: float = 10.0 * 60,
        interval_s: float = 1.0,
    ) -> V1Pod:
        async def _is_finished(pod: V1Pod) -> bool:
            return (pod.status.phase or "") in {_PodStatus.SUCCEEDED, _PodStatus.FAILED}

        return await self._wait_via_getter(
            is_satisfied=_is_finished,
            timeout_s=timeout_s,
            interval_s=interval_s,
        )

    async def wait_deleted(
        self,
        *,
        timeout_s: float = 10.0 * 60,
        interval_s: float = 1.0,
    ) -> None:
        async def _on_result(_: V1Pod) -> bool:
            return False

        async def _on_error(exc: KubeClientException) -> bool:
            # Treat both "not found" and "gone" as terminal deletion signals.
            return isinstance(exc, (ResourceNotFound, ResourceGone))

        await self._wait_via_getter_with_error_handler(
            on_result=_on_result,
            on_error=_on_error,
            timeout_s=timeout_s,
            interval_s=interval_s,
        )
        return None

    async def wait_terminated(
        self,
        *,
        timeout_s: float = 10.0 * 60,
        interval_s: float = 1.0,
        allow_pod_not_exists: bool = False,
    ) -> V1Pod | None:
        async def _any_terminated(pod: V1Pod) -> bool:
            statuses = []
            for s in pod.status.container_statuses:
                statuses.append(s.state.terminated is not None)
            for s in pod.status.init_container_statuses:
                statuses.append(s.state.terminated is not None)
            return bool(statuses) and all(statuses)

        if not allow_pod_not_exists:
            return await self._wait_via_getter(
                is_satisfied=_any_terminated,
                timeout_s=timeout_s,
                interval_s=interval_s,
            )

        async def _on_error(exc: KubeClientException) -> bool:
            return isinstance(exc, ResourceNotFound)

        return await self._wait_via_getter_with_error_handler(
            on_result=_any_terminated,
            on_error=_on_error,
            timeout_s=timeout_s,
            interval_s=interval_s,
        )

    async def wait_not_waiting(
        self,
        *,
        timeout_s: float = 10.0 * 60,
        interval_s: float = 1.0,
    ) -> V1Pod:
        async def _all_not_waiting(pod: V1Pod) -> bool:
            for s in pod.status.container_statuses:
                if s.state.waiting.__pydantic_fields_set__:
                    return False
            for s in pod.status.init_container_statuses:
                if s.state.waiting.__pydantic_fields_set__:
                    return False
            return True

        return await self._wait_via_getter(
            is_satisfied=_all_not_waiting,
            timeout_s=timeout_s,
            interval_s=interval_s,
        )

    async def wait_scheduled(
        self,
        *,
        timeout_s: float = 10.0 * 60,
        interval_s: float = 1.0,
    ) -> V1Pod:
        async def _is_scheduled(pod: V1Pod) -> bool:
            for cond in pod.status.conditions:
                if cond.type == "PodScheduled" and cond.status == "True":
                    return True
            return False

        return await self._wait_via_getter(
            is_satisfied=_is_scheduled,
            timeout_s=timeout_s,
            interval_s=interval_s,
        )

    async def _wait_via_getter_with_error_handler(
        self,
        *,
        on_result: Callable[[V1Pod], Awaitable[bool]],
        on_error: Callable[[KubeClientException], Awaitable[bool]] | None = None,
        timeout_s: float,
        interval_s: float,
    ) -> V1Pod | None:
        """
        Both `on_result` and `on_error` must return `True`
        for the waiter to be considered succeeded.
        """
        async with asyncio.timeout(timeout_s):
            while True:
                try:
                    pod = await self._parent.get(name=self._parent_resource_id)
                except KubeClientException as exc:
                    if on_error is None:
                        raise
                    done = await on_error(exc)
                    if done:
                        return None
                else:
                    done = await on_result(pod)
                    if done:
                        return pod

                await asyncio.sleep(interval_s)

    async def _wait_via_getter(
        self,
        *,
        is_satisfied: Callable[[V1Pod], Awaitable[bool]],
        timeout_s: float,
        interval_s: float,
    ) -> V1Pod:
        async def _on_result(pod: V1Pod) -> bool:
            res = await is_satisfied(pod)
            return bool(res)

        pod = await self._wait_via_getter_with_error_handler(
            on_result=_on_result,
            timeout_s=timeout_s,
            interval_s=interval_s,
        )
        assert pod is not None
        return pod
