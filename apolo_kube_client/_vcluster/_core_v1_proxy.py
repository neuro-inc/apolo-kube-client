import datetime
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from aiohttp import StreamReader

from .._apolo_waiters import ApoloPodWaiter
from .._constants import DEFAULT_TIMEOUT, DEFAULT_WAIT_INTERVAL
from .._core_v1 import (
    ConfigMap,
    CoreV1Api,
    Endpoint,
    Event,
    Namespace,
    PersistentVolumeClaim,
    Pod,
    PodLog,
    PodStatus,
    Secret,
    Service,
    ServiceAccount,
    ServiceAccountToken,
)
from .._models import (
    AuthenticationV1TokenRequest,
    CoreV1Event,
    CoreV1EventList,
    V1ConfigMap,
    V1ConfigMapList,
    V1Endpoints,
    V1EndpointsList,
    V1Namespace,
    V1NamespaceList,
    V1PersistentVolumeClaim,
    V1PersistentVolumeClaimList,
    V1Pod,
    V1PodList,
    V1Secret,
    V1SecretList,
    V1Service,
    V1ServiceAccount,
    V1ServiceAccountList,
    V1ServiceList,
    V1Status,
)
from ._attr_proxy import attr
from ._resource_proxy import (
    BaseProxy,
    ClusterScopedResourceProxy,
    NamespacedResourceProxy,
    NestedResourceProxy,
)


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


class ApoloPodWaiterProxy(NestedResourceProxy[V1Pod, ApoloPodWaiter]):
    async def wait_running(
        self,
        *,
        timeout_s: float = DEFAULT_TIMEOUT,
        interval_s: float = DEFAULT_WAIT_INTERVAL,
    ) -> V1Pod:
        return await self._origin.wait_running(
            timeout_s=timeout_s,
            interval_s=interval_s,
        )

    async def wait_finished(
        self,
        *,
        timeout_s: float = DEFAULT_TIMEOUT,
        interval_s: float = DEFAULT_WAIT_INTERVAL,
    ) -> V1Pod:
        return await self._origin.wait_finished(
            timeout_s=timeout_s,
            interval_s=interval_s,
        )

    async def wait_deleted(
        self,
        *,
        timeout_s: float = DEFAULT_TIMEOUT,
        interval_s: float = DEFAULT_WAIT_INTERVAL,
    ) -> None:
        return await self._origin.wait_deleted(
            timeout_s=timeout_s,
            interval_s=interval_s,
        )

    async def wait_terminated(
        self,
        *,
        timeout_s: float = DEFAULT_TIMEOUT,
        interval_s: float = DEFAULT_WAIT_INTERVAL,
        allow_pod_not_exists: bool = False,
    ) -> V1Pod | None:
        return await self._origin.wait_terminated(
            timeout_s=timeout_s,
            interval_s=interval_s,
            allow_pod_not_exists=allow_pod_not_exists,
        )

    async def wait_not_waiting(
        self,
        *,
        timeout_s: float = DEFAULT_TIMEOUT,
        interval_s: float = DEFAULT_WAIT_INTERVAL,
    ) -> V1Pod:
        return await self._origin.wait_not_waiting(
            timeout_s=timeout_s,
            interval_s=interval_s,
        )

    async def wait_scheduled(
        self,
        *,
        timeout_s: float = DEFAULT_TIMEOUT,
        interval_s: float = DEFAULT_WAIT_INTERVAL,
    ) -> V1Pod:
        return await self._origin.wait_scheduled(
            timeout_s=timeout_s,
            interval_s=interval_s,
        )


class PodProxy(NamespacedResourceProxy[V1Pod, V1PodList, V1Pod, Pod]):
    @attr(PodStatusProxy)
    def status(self) -> PodStatus:
        return self._origin.status

    @attr(PodLogProxy)
    def log(self) -> PodLog:
        return self._origin.log

    @attr(ApoloPodWaiterProxy)
    def apolo_waiter(self) -> ApoloPodWaiter:
        return self._origin.apolo_waiter


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


class ConfigMapProxy(
    NamespacedResourceProxy[V1ConfigMap, V1ConfigMapList, V1Status, ConfigMap]
):
    async def add_key(
        self,
        name: str,
        key: str,
        value: str,
    ) -> V1ConfigMap:
        return await self._origin.add_key(
            name=name,
            key=key,
            value=value,
            namespace=self._namespace,
        )

    async def delete_key(self, name: str, key: str) -> V1ConfigMap:
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


class ServiceAccountTokenProxy(
    NestedResourceProxy[AuthenticationV1TokenRequest, ServiceAccountToken]
):
    async def create(
        self,
        model: AuthenticationV1TokenRequest,
    ) -> AuthenticationV1TokenRequest:
        return await self._origin.create(model, namespace=self._namespace)


class ServiceAccountProxy(
    NamespacedResourceProxy[
        V1ServiceAccount,
        V1ServiceAccountList,
        V1Status,
        ServiceAccount,
    ]
):
    @attr(ServiceAccountTokenProxy)
    def token(self) -> ServiceAccountToken:
        return self._origin.token


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


class NamespaceProxy(
    ClusterScopedResourceProxy[
        V1Namespace,
        V1NamespaceList,
        V1Namespace,
        Namespace,
    ]
):
    pass


class CoreV1ApiProxy(BaseProxy[CoreV1Api]):
    """
    Core v1 API wrapper for Kubernetes.
    """

    # cluster scoped resources
    @attr(NamespaceProxy)
    def namespace(self) -> Namespace:
        return self._origin.namespace

    # namespaced resources
    @attr(PodProxy)
    def pod(self) -> Pod:
        return self._origin.pod

    @attr(SecretProxy)
    def secret(self) -> Secret:
        return self._origin.secret

    @attr(ConfigMapProxy)
    def config_map(self) -> ConfigMap:
        return self._origin.config_map

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

    @attr(ServiceAccountProxy)
    def serviceaccounts(self) -> ServiceAccount:
        return self._origin.serviceaccounts

    # ASvetlov: CoreV1Api has cluster-scoped networking_k8s_io_v1 and discovery_k8s_io_v1
    # Not sure if we should expose these attrs in project-scoped client.
    # Most likely it doesn't make any sense.
    # Anyway, we could add them later.
