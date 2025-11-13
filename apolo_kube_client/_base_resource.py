import functools
from collections.abc import AsyncIterator, Collection
from contextlib import asynccontextmanager
from typing import ClassVar, cast, get_args
from typing import Self

import aiohttp
from yarl import URL

from ._core import KubeCore
from ._errors import ResourceNotFound
from ._typedefs import JsonType
from ._watch import Watch
from ._models import ResourceModel, ListModel


class Base:
    def __init__(self, core: KubeCore) -> None:
        self._core = core


class ModelClassMixin[
    ModelT: ResourceModel | str | None,
    ListModelT: ListModel | str | None,
    DeleteModelT: ListModel | ResourceModel | str | None,
]:
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

    @property
    def _delete_model_class(self) -> type[DeleteModelT]:
        if hasattr(self, "__orig_class__"):
            return cast(type[DeleteModelT], get_args(self.__orig_class__)[2])
        if hasattr(self, "__orig_bases__"):
            return cast(type[DeleteModelT], get_args(self.__orig_bases__[0])[2])
        raise ValueError("DeleteModel class not found")


class BaseResource[
    ModelT: ResourceModel,
    ListModelT: ListModel,
    DeleteModelT: ListModel | ResourceModel,
](ModelClassMixin[ModelT, ListModelT, DeleteModelT]):
    """
    Base class for Kubernetes resources
    Uses models from the official Kubernetes API client.
    """

    query_path: ClassVar[str]

    def __init__(
        self,
        core: KubeCore,
        group_api_query_path: str,
        resource_id: str | None = None,
    ):
        if not self.query_path:
            raise ValueError("resource api query_path must be set")

        self._core: KubeCore = core
        self._group_api_query_path: str = group_api_query_path
        self._resource_id = resource_id

    def __getitem__(self, resource_id: str) -> Self:
        """
        Returns a resource instance bound to a concrete resource_id.

        Usage:
        >>> kube_client.core_v1.pod["pod-name"]
        """
        if self._resource_id is not None:
            raise ValueError(f"kube client was already bound to {self._resource_id}")
        return self.__class__(self._core, self._group_api_query_path, resource_id)

    async def get(self, name: str) -> ModelT:
        raise NotImplementedError

    async def get_list(self) -> ListModelT:
        raise NotImplementedError

    def watch(self) -> Watch[ModelT]:
        raise NotImplementedError

    async def create(self, model: ModelT) -> ModelT:
        raise NotImplementedError

    async def delete(self, name: str) -> DeleteModelT:
        raise NotImplementedError


class ClusterScopedResource[
    ModelT: ResourceModel,
    ListModelT: ListModel,
    DeleteModelT: ListModel | ResourceModel,
](BaseResource[ModelT, ListModelT, DeleteModelT]):
    """
    Base class for Kubernetes resources that are not namespaced (cluster scoped).
    """

    def _build_url_list(self) -> URL:
        assert self.query_path, "query_path must be set"
        return self._core.base_url / self._group_api_query_path / self.query_path

    def _build_url(self, name: str) -> URL:
        return self._build_url_list() / name

    async def get(self, name: str) -> ModelT:
        async with self._core.request(method="GET", url=self._build_url(name)) as resp:
            return await self._core.deserialize_response(resp, self._model_class)

    async def get_list(self, label_selector: str | None = None) -> ListModelT:
        params = {"labelSelector": label_selector} if label_selector else None
        async with self._core.request(
            method="GET", url=self._build_url_list(), params=params
        ) as resp:
            return await self._core.deserialize_response(resp, self._list_model_class)

    @asynccontextmanager
    async def _get_watch(
        self,
        label_selector: str | None = None,
        resource_version: str | None = None,
        allow_watch_bookmarks: bool = False,
    ) -> AsyncIterator[aiohttp.ClientResponse]:
        params = {
            "watch": "1",
            "allowWatchBookmarks": str(allow_watch_bookmarks).lower(),
        }
        if resource_version:
            params["resourceVersion"] = resource_version
        if label_selector:
            params["labelSelector"] = label_selector
        async with self._core.request(
            method="GET",
            url=self._build_url_list(),
            params=params,
        ) as resp:
            yield resp

    def watch(
        self,
        label_selector: str | None = None,
        resource_version: str | None = None,
        allow_watch_bookmarks: bool = False,
    ) -> Watch[ModelT]:
        return Watch(
            resource_version=resource_version,
            get_response=functools.partial(
                self._get_watch,
                label_selector=label_selector,
                allow_watch_bookmarks=allow_watch_bookmarks,
            ),
            deserialize=functools.partial(
                self._core.deserialize, klass=self._model_class
            ),
        )

    async def create(self, model: ModelT) -> ModelT:
        async with self._core.request(
            method="POST",
            url=self._build_url_list(),
            json=self._core.serialize(model),
        ) as resp:
            return await self._core.deserialize_response(resp, self._model_class)

    async def delete(
        self, name: str, *, payload: JsonType | None = None
    ) -> DeleteModelT:
        async with self._core.request(
            method="DELETE", url=self._build_url(name), json=payload
        ) as resp:
            return await self._core.deserialize_response(resp, self._delete_model_class)

    async def get_or_create(self, model: ModelT) -> tuple[bool, ModelT]:
        """
        Get a resource by name, or create it if it does not exist.
        Returns a tuple (created, model).
        """
        assert model.metadata.name is not None, model.metadata.name
        try:
            return False, await self.get(name=model.metadata.name)
        except ResourceNotFound:
            return True, await self.create(model)

    async def update(self, model: ModelT) -> ModelT:
        assert model.metadata.name is not None
        async with self._core.request(
            method="PUT",
            url=self._build_url(model.metadata.name),
            json=self._core.serialize(model),
        ) as resp:
            return await self._core.deserialize_response(resp, self._model_class)

    async def create_or_update(self, model: ModelT) -> tuple[bool, ModelT]:
        """
        Create or update a resource.
        If the resource exists, it will be updated.
        Returns a tuple (created, model).
        """
        assert model.metadata.name is not None, model.metadata.name
        try:
            await self.get(name=model.metadata.name)
            async with self._core.request(
                method="PATCH",
                headers={"Content-Type": "application/strategic-merge-patch+json"},
                url=self._build_url(model.metadata.name),
                json=self._core.serialize(model),
            ) as resp:
                return False, await self._core.deserialize_response(
                    resp, self._model_class
                )
        except ResourceNotFound:
            return True, await self.create(model)

    async def patch_json(
        self, name: str, patch_json_list: list[dict[str, str]]
    ) -> ModelT:
        """
        Patch a resource with a JSON patch.
        RFC 6902 defines the JSON Patch format.
        """
        async with self._core.request(
            method="PATCH",
            headers={"Content-Type": "application/json-patch+json"},
            url=self._build_url(name),
            json=cast(JsonType, patch_json_list),
        ) as resp:
            return await self._core.deserialize_response(resp, self._model_class)


class NamespacedResource[
    ModelT: ResourceModel,
    ListModelT: ListModel,
    DeleteModelT: ListModel | ResourceModel,
](BaseResource[ModelT, ListModelT, DeleteModelT]):
    """
    Base class for Kubernetes resources that are namespaced.
    """

    def _build_url_list(self, namespace: str | None) -> URL:
        assert self.query_path, "query_path must be set"
        base_url = self._core.base_url / self._group_api_query_path
        if not namespace:
            return base_url / self.query_path
        return base_url / "namespaces" / namespace / self.query_path

    def _build_url(self, name: str, namespace: str) -> URL:
        return self._build_url_list(namespace) / name

    def _get_ns(self, namespace: str | None = None) -> str:
        return self._core.resolve_namespace(namespace)

    async def get(self, name: str, namespace: str | None = None) -> ModelT:
        async with self._core.request(
            method="GET", url=self._build_url(name, self._get_ns(namespace))
        ) as resp:
            return await self._core.deserialize_response(resp, self._model_class)

    async def get_list(
        self,
        label_selector: str | None = None,
        field_selector: str | None = None,
        namespace: str | None = None,
        all_namespaces: bool = False,
    ) -> ListModelT:
        params = {}
        if label_selector:
            params["labelSelector"] = label_selector
        if field_selector:
            params["fieldSelector"] = field_selector
        async with self._core.request(
            method="GET",
            url=self._build_url_list(
                None if all_namespaces else self._get_ns(namespace)
            ),
            params=params,
        ) as resp:
            return await self._core.deserialize_response(resp, self._list_model_class)

    @asynccontextmanager
    async def _get_watch(
        self,
        label_selector: str | None = None,
        namespace: str | None = None,
        all_namespaces: bool = False,
        resource_version: str | None = None,
        allow_watch_bookmarks: bool = False,
    ) -> AsyncIterator[aiohttp.ClientResponse]:
        params = {
            "watch": "1",
            "allowWatchBookmarks": str(allow_watch_bookmarks).lower(),
        }
        if resource_version:
            params["resourceVersion"] = resource_version
        if label_selector:
            params["labelSelector"] = label_selector
        async with self._core.request(
            method="GET",
            url=self._build_url_list(
                None if all_namespaces else self._get_ns(namespace)
            ),
            params=params,
        ) as resp:
            yield resp

    def watch(
        self,
        label_selector: str | None = None,
        all_namespaces: bool = False,
        namespace: str | None = None,
        resource_version: str | None = None,
        allow_watch_bookmarks: bool = False,
    ) -> Watch[ModelT]:
        return Watch(
            resource_version=resource_version,
            get_response=functools.partial(
                self._get_watch,
                label_selector=label_selector,
                all_namespaces=all_namespaces,
                namespace=namespace,
                allow_watch_bookmarks=allow_watch_bookmarks,
            ),
            deserialize=functools.partial(
                self._core.deserialize, klass=self._model_class
            ),
        )

    async def create(self, model: ModelT, namespace: str | None = None) -> ModelT:
        async with self._core.request(
            method="POST",
            url=self._build_url_list(self._get_ns(namespace)),
            json=self._core.serialize(model),
        ) as resp:
            return await self._core.deserialize_response(resp, self._model_class)

    async def delete(
        self,
        name: str,
        namespace: str | None = None,
        *,
        payload: JsonType | None = None,
    ) -> DeleteModelT:
        async with self._core.request(
            method="DELETE",
            url=self._build_url(name, self._get_ns(namespace)),
            json=payload,
        ) as resp:
            return await self._core.deserialize_response(resp, self._delete_model_class)

    async def get_or_create(
        self, model: ModelT, namespace: str | None = None
    ) -> tuple[bool, ModelT]:
        """
        Get a resource by name, or create it if it does not exist.
        Returns a tuple (created, model).
        """
        assert model.metadata.name is not None, model.metadata.name
        try:
            return False, await self.get(name=model.metadata.name, namespace=namespace)
        except ResourceNotFound:
            return True, await self.create(model, namespace=namespace)

    async def update(self, model: ModelT, namespace: str | None = None) -> ModelT:
        assert model.metadata.name is not None
        async with self._core.request(
            method="PUT",
            url=self._build_url(model.metadata.name, self._get_ns(namespace)),
            json=self._core.serialize(model),
        ) as resp:
            return await self._core.deserialize_response(resp, self._model_class)

    async def create_or_update(
        self, model: ModelT, namespace: str | None = None
    ) -> tuple[bool, ModelT]:
        """
        Create or update a resource.
        If the resource exists, it will be updated.
        Returns a tuple (created, model).
        """
        assert model.metadata.name is not None, model.metadata.name
        try:
            await self.get(name=model.metadata.name, namespace=namespace)
            async with self._core.request(
                method="PATCH",
                headers={"Content-Type": "application/strategic-merge-patch+json"},
                url=self._build_url(model.metadata.name, self._get_ns(namespace)),
                json=self._core.serialize(model),
            ) as resp:
                return False, await self._core.deserialize_response(
                    resp, self._model_class
                )
        except ResourceNotFound:
            return True, await self.create(model, namespace=namespace)

    async def patch_json(
        self,
        name: str,
        patch_json_list: list[dict[str, str | Collection[str]]],
        namespace: str | None = None,
    ) -> ModelT:
        """
        Patch a resource with a JSON patch.
        RFC 6902 defines the JSON Patch format.
        """
        async with self._core.request(
            method="PATCH",
            headers={"Content-Type": "application/json-patch+json"},
            url=self._build_url(name, self._get_ns(namespace)),
            json=cast(JsonType, patch_json_list),
        ) as resp:
            return await self._core.deserialize_response(resp, self._model_class)


class NestedResource[
    ModelT: ResourceModel,
](ModelClassMixin[ModelT, None, None]):
    is_nested_resource = True  # marker
    query_path: ClassVar[str]

    def __init__(
        self,
        parent: (  # type: ignore[type-var]
            NamespacedResource[ModelT, None, None]
            | ClusterScopedResource[ModelT, None, None]
        ),
    ):
        self._core = parent._core
        self._group_api_query_path = parent._group_api_query_path
        self._parent = parent
        rid = getattr(parent, "_resource_id", None)
        if not rid:
            raise ValueError("Nested resource requires parent resource_id")
        self._parent_resource_id: str = rid

    def _build_url(self, namespace: str | None = None) -> URL:
        assert self.query_path, "query_path must be set"
        parent = self._parent
        if isinstance(parent, NamespacedResource):
            base = parent._build_url(
                self._parent_resource_id, parent._get_ns(namespace)
            )
        else:
            base = parent._build_url(self._parent_resource_id)
        return base / self.query_path

    async def get(
        self,
        namespace: str | None = None,
    ) -> ModelT:
        async with self._core.request(
            method="GET", url=self._build_url(namespace)
        ) as resp:
            return await self._core.deserialize_response(resp, self._model_class)

    async def update(
        self,
        model: ModelT,
        namespace: str | None = None,
    ) -> ModelT:
        async with self._core.request(
            method="PUT",
            url=self._build_url(namespace),
            json=self._core.serialize(model),
        ) as resp:
            return await self._core.deserialize_response(resp, self._model_class)
