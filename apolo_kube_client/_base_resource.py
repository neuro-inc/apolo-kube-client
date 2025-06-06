from typing import Any, Generic, Protocol, TypeVar, cast, get_args, overload

import aiohttp
from kubernetes.client import ApiClient, models as available_k8s_models
from yarl import URL

from apolo_kube_client._core import _KubeCore


class HasToDict(Protocol):
    def to_dict(self) -> dict[str, Any]: ...


ModelT = TypeVar("ModelT", bound=HasToDict)
ListModelT = TypeVar("ListModelT", bound=HasToDict)


class _RESTResponse:
    """
    This is our custom analogue of the `kubernetes.client.rest.RESTResponse` class
    that is used for deserializing response data from the Kubernetes API.
    Aiohttp Response instead of the urllib3 Response
    """

    def __init__(self, resp: aiohttp.ClientResponse, data: bytes):
        self.response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = data


class BaseResource(Generic[ModelT, ListModelT]):
    """
    Base class for Kubernetes resources
    Uses models from the official Kubernetes API client.
    """

    query_path: str

    def __init__(
        self, core: _KubeCore, group_api_query_path: str, api_client: ApiClient
    ):
        if not self.query_path:
            raise ValueError("resource api query_path must be set")

        self._core: _KubeCore = core
        self._group_api_query_path: str = group_api_query_path
        self._api_client = api_client

    @property
    def _model_class(self) -> type[ModelT]:
        if hasattr(self, "__orig_class__"):
            return cast(type[ModelT], get_args(self.__orig_class__)[0])
        if hasattr(self, "__orig_bases__"):
            return cast(type[ModelT], get_args(self.__orig_bases__[0])[0])
        raise ValueError("Model class not found")

    @property
    def _list_model_class(self) -> type[ListModelT]:
        if hasattr(self, "__orig_class__"):
            return cast(type[ListModelT], get_args(self.__orig_class__)[1])
        if hasattr(self, "__orig_bases__"):
            return cast(type[ListModelT], get_args(self.__orig_bases__[0])[1])
        raise ValueError("ListModel class not found")

    @overload
    async def _deserialize(
        self, response: aiohttp.ClientResponse, response_type: type[ModelT]
    ) -> ModelT: ...

    @overload
    async def _deserialize(
        self, response: aiohttp.ClientResponse, response_type: type[ListModelT]
    ) -> ListModelT: ...

    async def _deserialize(
        self,
        response: aiohttp.ClientResponse,
        response_type: type[ModelT] | type[ListModelT],
    ) -> ModelT | ListModelT:
        if not hasattr(available_k8s_models, response_type.__name__):
            raise ValueError(f"Unsupported response type: {response_type}")
        rest_response = _RESTResponse(response, await response.read())
        return cast(
            ModelT | ListModelT,
            self._api_client.deserialize(rest_response, response_type),
        )

    def _build_url_list(self, *args: Any, **kwargs: Any) -> URL:
        raise NotImplementedError

    def _build_url(self, *args: Any, **kwargs: Any) -> URL:
        raise NotImplementedError

    async def get(self, *args: Any, **kwargs: Any) -> ModelT:
        raise NotImplementedError

    async def list(self, *args: Any, **kwargs: Any) -> ListModelT:
        raise NotImplementedError

    async def create(self, *args: Any, **kwargs: Any) -> ModelT:
        raise NotImplementedError

    async def delete(self, *args: Any, **kwargs: Any) -> ModelT:
        raise NotImplementedError


class ClusterScopedResource(BaseResource[ModelT, ListModelT]):
    def _build_url_list(self) -> URL:
        assert self.query_path, "query_path must be set"
        return self._core.base_url / self._group_api_query_path / self.query_path

    def _build_url(self, name: str) -> URL:
        return self._build_url_list() / name

    async def get(self, name: str) -> ModelT:
        resp = await self._core.request(method="GET", url=self._build_url(name))
        return await self._deserialize(resp, self._model_class)

    async def list(self) -> ListModelT:
        resp = await self._core.request(method="GET", url=self._build_url_list())
        return await self._deserialize(resp, self._list_model_class)

    async def create(self, model: ModelT) -> ModelT:
        resp = await self._core.request(
            method="POST", url=self._build_url_list(), json=model.to_dict()
        )
        return await self._deserialize(resp, self._model_class)

    async def delete(self, name: str) -> ModelT:
        resp = await self._core.request(method="DELETE", url=self._build_url(name))
        return await self._deserialize(resp, self._model_class)


class NamespacedResource(BaseResource[ModelT, ListModelT]):
    def _build_url_list(self, namespace: str) -> URL:
        assert self.query_path, "query_path must be set"
        return (
            self._core.base_url
            / self._group_api_query_path
            / "namespaces"
            / namespace
            / self.query_path
        )

    def _build_url(self, name: str, namespace: str) -> URL:
        return self._build_url_list(namespace) / name

    def _get_ns(self, namespace: str | None = None) -> str:
        return namespace or self._core.namespace

    async def get(self, name: str, namespace: str | None = None) -> ModelT:
        resp = await self._core.request(
            method="GET", url=self._build_url(name, self._get_ns(namespace))
        )
        return await self._deserialize(resp, self._model_class)

    async def list(self, namespace: str | None = None) -> ListModelT:
        resp = await self._core.request(
            method="GET", url=self._build_url_list(self._get_ns(namespace))
        )
        return await self._deserialize(resp, self._list_model_class)

    async def create(self, model: ModelT, namespace: str | None = None) -> ModelT:
        resp = await self._core.request(
            method="POST",
            url=self._build_url_list(self._get_ns(namespace)),
            json=model.to_dict(),
        )
        return await self._deserialize(resp, self._model_class)

    async def delete(self, name: str, namespace: str | None = None) -> ModelT:
        resp = await self._core.request(
            method="DELETE", url=self._build_url(name, self._get_ns(namespace))
        )
        return await self._deserialize(resp, self._model_class)
