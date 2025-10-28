import datetime
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from aiohttp import StreamReader
from .._core_v1 import (
    CoreV1Api,
    Endpoint,
    Event,
    PersistentVolumeClaim,
    Pod,
    PodLog,
    PodStatus,
    Secret,
    Service,
)
from ._attr_proxy import attr
from ._resource_proxy import BaseProxy, NamespacedResourceProxy
from .._models import (
    CoreV1Event,
    CoreV1EventList,
    V1Endpoints,
    V1EndpointsList,
    V1PersistentVolumeClaim,
    V1PersistentVolumeClaimList,
    V1Pod,
    V1PodList,
    V1Secret,
    V1SecretList,
    V1Service,
    V1ServiceList,
    V1Status,
)

from ._resource_proxy import NestedResourceProxy


class PodStatusProxy(NestedResourceProxy[V1Pod, PodStatus]):
    pass


class PodLogProxy(NestedResourceProxy[V1Pod, PodLog]):
    async def read(
        self,
        *,
        container: str | None = None,
        follow: bool | None = None,
        previous: bool | None = None,
        timestamps: bool | None = None,
        since: datetime.datetime | None = None,
    ) -> str:
        return await self._origin.read(
            container=container,
            follow=follow,
            previous=previous,
            timestamps=timestamps,
            since=since,
            namespace=self._namespace,
        )

    @asynccontextmanager
    async def stream(
        self,
        *,
        container: str | None = None,
        follow: bool | None = None,
        previous: bool | None = None,
        timestamps: bool | None = None,
        since: datetime.datetime | None = None,
    ) -> AsyncIterator[StreamReader]:
        async with self._origin.stream(
            container=container,
            follow=follow,
            previous=previous,
            timestamps=timestamps,
            since=since,
            namespace=self._namespace,
        ) as stream:
            yield stream


class PodProxy(NamespacedResourceProxy[V1Pod, V1PodList, V1Pod, Pod]):
    @attr(PodStatusProxy)
    def status(self) -> PodStatus:
        return self._origin.status

    @attr(PodLogProxy)
    def log(self) -> PodLog:
        return self._origin.log


class SecretProxy(NamespacedResourceProxy[V1Secret, V1SecretList, V1Status, Secret]):
    async def add_key(
        self,
        name: str,
        key: str,
        value: str,
        *,
        encode: bool = True,
    ) -> V1Secret:
        return await self._origin.add_key(
            name=name, key=key, value=value, encode=encode, namespace=self._namespace
        )

    async def delete_key(self, name: str, key: str) -> V1Secret:
        return await self._origin.delete_key(
            name=name,
            key=key,
            namespace=self._namespace,
        )


class PersistentVolumeClaimProxy(
    NamespacedResourceProxy[
        V1PersistentVolumeClaim,
        V1PersistentVolumeClaimList,
        V1PersistentVolumeClaim,
        PersistentVolumeClaim,
    ]
):
    pass


class ServiceProxy(
    NamespacedResourceProxy[
        V1Service,
        V1ServiceList,
        V1Service,
        Service,
    ]
):
    pass


class EventProxy(
    NamespacedResourceProxy[
        CoreV1Event,
        CoreV1EventList,
        V1Status,
        Event,
    ]
):
    pass


class EndpointProxy(
    NamespacedResourceProxy[
        V1Endpoints,
        V1EndpointsList,
        V1Endpoints,
        Endpoint,
    ]
):
    pass


class CoreV1ApiProxy(BaseProxy[CoreV1Api]):
    """
    Core v1 API wrapper for Kubernetes.
    """

    # cluster scoped resources
    # namespaced resources
    @attr(PodProxy)
    def pod(self) -> Pod:
        return self._origin.pod

    @attr(SecretProxy)
    def secret(self) -> Secret:
        return self._origin.secret

    @attr(PersistentVolumeClaimProxy)
    def persistent_volume_claim(self) -> PersistentVolumeClaim:
        return self._origin.persistent_volume_claim

    @attr(ServiceProxy)
    def service(self) -> Service:
        return self._origin.service

    @attr(EndpointProxy)
    def endpoint(self) -> Endpoint:
        return self._origin.endpoint

    @attr(EventProxy)
    def event(self) -> Event:
        return self._origin.event

    # ASvetlov: CoreV1Api has cluster-scoped networking_k8s_io_v1 and discovery_k8s_io_v1
    # Not sure if we should expose these attrs in project-scoped client.
    # Most likely it doesn't make any sense.
    # Anyway, we could add them later.
