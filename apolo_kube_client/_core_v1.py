import datetime
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Annotated

from aiohttp import StreamReader
from pydantic import BaseModel, ConfigDict, Field

from ._apolo_waiters import ApoloPodWaiter
from ._attr import _Attr
from ._base_resource import (
    Base,
    ClusterScopedResource,
    NamespacedResource,
    NestedResource,
    PatchAdd,
    PatchOps,
    PatchRemove,
)
from ._models import (
    AuthenticationV1TokenRequest,
    CoreV1Event,
    CoreV1EventList,
    V1ConfigMap,
    V1ConfigMapList,
    V1Endpoints,
    V1EndpointsList,
    V1Namespace,
    V1NamespaceList,
    V1Node,
    V1NodeList,
    V1PersistentVolume,
    V1PersistentVolumeClaim,
    V1PersistentVolumeClaimList,
    V1PersistentVolumeList,
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
from ._utils import base64_encode, escape_json_pointer


class Namespace(ClusterScopedResource[V1Namespace, V1NamespaceList, V1Namespace]):
    query_path = "namespaces"


class StatsBaseModel(BaseModel):
    model_config = ConfigDict(
        extra="allow",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )


class StatsSwap(StatsBaseModel):
    swap_available_bytes: Annotated[int, Field(alias="swapAvailableBytes")] = -1
    swap_usage_bytes: Annotated[int, Field(alias="swapUsageBytes")] = -1
    time: datetime.datetime


class StatsPodRef(StatsBaseModel):
    name: str
    namespace: str


class StatsVolumePVC(StatsBaseModel):
    name: str


class StatsVolume(StatsBaseModel):
    pvc_ref: Annotated[StatsVolumePVC | None, Field(alias="pvcRef")] = None
    used_bytes: Annotated[int, Field(alias="usedBytes")]


class StatsPod(StatsBaseModel):
    pod_ref: Annotated[StatsPodRef, Field(alias="podRef")]
    swap: StatsSwap | None = None
    volume: list[StatsVolume] = []


class StatsNode(StatsBaseModel):
    swap: StatsSwap | None = None


class StatsSummary(StatsBaseModel):
    node: StatsNode
    pods: list[StatsPod] = []


class Node(ClusterScopedResource[V1Node, V1NodeList, V1Status]):
    query_path = "nodes"

    async def get_stats_summary(self, name: str) -> StatsSummary:
        dct = await self._core.get(
            url=self._build_url(name) / "proxy" / "stats" / "summary",
        )
        return StatsSummary.model_validate(dct)


class PodStatus(NestedResource[V1Pod]):
    query_path = "status"


class PodLog(NestedResource[V1Pod]):
    query_path = "log"

    async def read(
        self,
        *,
        container: str | None = None,
        follow: bool | None = None,
        previous: bool | None = None,
        timestamps: bool | None = None,
        since: datetime.datetime | None = None,
        namespace: str | None = None,
    ) -> str:
        params: dict[str, str | bool] = {}
        if container is not None:
            params["container"] = container
        if follow is not None:
            params["follow"] = str(follow).lower()
        if previous is not None:
            params["previous"] = str(previous).lower()
        if timestamps is not None:
            params["timestamps"] = str(timestamps).lower()
        if since is not None:
            params["sinceTime"] = since.isoformat().replace("+00:00", "Z")
        async with self._core.request(
            method="GET",
            url=self._build_url(namespace),
            params=params,
        ) as resp:
            return (await resp.read()).decode("utf-8")

    @asynccontextmanager
    async def stream(
        self,
        *,
        container: str | None = None,
        follow: bool | None = None,
        previous: bool | None = None,
        timestamps: bool | None = None,
        since: datetime.datetime | None = None,
        namespace: str | None = None,
    ) -> AsyncIterator[StreamReader]:
        params: dict[str, str | bool] = {}
        if container is not None:
            params["container"] = container
        if follow is not None:
            params["follow"] = str(follow).lower()
        if previous is not None:
            params["previous"] = str(previous).lower()
        if timestamps is not None:
            params["timestamps"] = str(timestamps).lower()
        if since is not None:
            params["sinceTime"] = since.isoformat().replace("+00:00", "Z")
        async with self._core.request(
            method="GET",
            url=self._build_url(namespace),
            params=params,
        ) as resp:
            yield resp.content


class Pod(NamespacedResource[V1Pod, V1PodList, V1Pod]):
    query_path = "pods"
    status = _Attr(PodStatus)
    log = _Attr(PodLog)
    apolo_waiter = _Attr(ApoloPodWaiter)


class ServiceAccountToken(NestedResource[AuthenticationV1TokenRequest]):
    query_path = "token"

    async def create(
        self,
        model: AuthenticationV1TokenRequest,
        *,
        namespace: str | None = None,
    ) -> AuthenticationV1TokenRequest:
        async with self._core.request(
            method="POST",
            url=self._build_url(namespace),
            json=self._core.serialize(model),
        ) as resp:
            return await self._core.deserialize_response(resp, self._model_class)


class ServiceAccount(
    NamespacedResource[V1ServiceAccount, V1ServiceAccountList, V1ServiceAccount],
):
    query_path = "serviceaccounts"
    token = _Attr(ServiceAccountToken)


class Secret(NamespacedResource[V1Secret, V1SecretList, V1Status]):
    query_path = "secrets"

    async def add_key(
        self,
        name: str,
        key: str,
        value: str,
        *,
        namespace: str,
        encode: bool = True,
    ) -> V1Secret:
        secret = await self.get(name=name, namespace=self._get_ns(namespace))
        patch_json_list: list[PatchOps] = []
        if "data" not in secret.__pydantic_fields_set__:
            patch_json_list.append(PatchAdd(path="/data", value={}))
        patch_json_list.append(
            PatchAdd(
                path=f"/data/{escape_json_pointer(key)}",
                value=base64_encode(value) if encode else value,
            )
        )
        return await self.patch_json(
            name=name,
            patch_json_list=patch_json_list,
            namespace=self._get_ns(namespace),
        )

    async def delete_key(self, name: str, key: str, *, namespace: str) -> V1Secret:
        return await self.patch_json(
            name=name,
            patch_json_list=[PatchRemove(path=f"/data/{escape_json_pointer(key)}")],
            namespace=self._get_ns(namespace),
        )


class ConfigMap(
    NamespacedResource[V1ConfigMap, V1ConfigMapList, V1Status],
):
    query_path = "configmaps"

    async def add_key(
        self,
        name: str,
        key: str,
        value: str,
        *,
        namespace: str,
    ) -> V1ConfigMap:
        config_map = await self.get(name=name, namespace=self._get_ns(namespace))
        patch_json_list: list[PatchOps] = []
        if "data" not in config_map.__pydantic_fields_set__:
            patch_json_list.append(PatchAdd(path="/data", value={}))
        patch_json_list.append(
            PatchAdd(
                path=f"/data/{escape_json_pointer(key)}",
                value=value,
            )
        )
        return await self.patch_json(
            name=name,
            patch_json_list=patch_json_list,
            namespace=self._get_ns(namespace),
        )

    async def delete_key(self, name: str, key: str, *, namespace: str) -> V1ConfigMap:
        return await self.patch_json(
            name=name,
            patch_json_list=[PatchRemove(path=f"/data/{escape_json_pointer(key)}")],
            namespace=self._get_ns(namespace),
        )


class PersistentVolume(
    ClusterScopedResource[
        V1PersistentVolume, V1PersistentVolumeList, V1PersistentVolume
    ]
):
    query_path = "persistentvolumes"


class PersistentVolumeClaim(
    NamespacedResource[
        V1PersistentVolumeClaim, V1PersistentVolumeClaimList, V1PersistentVolumeClaim
    ]
):
    query_path = "persistentvolumeclaims"


class Service(NamespacedResource[V1Service, V1ServiceList, V1Service]):
    query_path = "services"


class Endpoint(NamespacedResource[V1Endpoints, V1EndpointsList, V1Endpoints]):
    query_path = "endpoints"


class Event(NamespacedResource[CoreV1Event, CoreV1EventList, CoreV1Event]):
    query_path = "events"


class CoreV1Api(Base):
    """
    Core v1 API wrapper for Kubernetes.
    """

    group_api_query_path = "api/v1"
    # cluster scoped resources
    namespace = _Attr(Namespace, group_api_query_path)
    node = _Attr(Node, group_api_query_path)
    persistent_volume = _Attr(PersistentVolume, group_api_query_path)
    # namespaced resources
    pod = _Attr(Pod, group_api_query_path)
    secret = _Attr(Secret, group_api_query_path)
    config_map = _Attr(ConfigMap, group_api_query_path)
    persistent_volume_claim = _Attr(PersistentVolumeClaim, group_api_query_path)
    service = _Attr(Service, group_api_query_path)
    endpoint = _Attr(Endpoint, group_api_query_path)
    event = _Attr(Event, group_api_query_path)
    serviceaccounts = _Attr(ServiceAccount, group_api_query_path)
