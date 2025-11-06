from collections.abc import Collection
from typing import Self, cast

from .._base_resource import NamespacedResource
from .._models import ResourceModel, ListModel
from .._base_resource import NestedResource
from .._typedefs import JsonType
from .._watch import Watch


class BaseProxy[OriginT]:
    def __init__(
        self,
        origin: OriginT,
        namespace: str,
        *,
        is_vcluster: bool,
        resource_id: str | None = None,
    ):
        self.is_vcluster = is_vcluster
        self._origin = origin
        self._namespace = namespace  # 'default' for vcluster projects
        self._resource_id = resource_id

    def __getitem__(self, resource_id: str) -> Self:
        if self._resource_id is not None:
            raise ValueError(f"kube client was already bound to {self._resource_id}")
        # create a new origin and bound it to a specific resource ID
        bound_origin = self._origin[resource_id]  # type: ignore[index]
        return self.__class__(
            bound_origin,
            self._namespace,
            is_vcluster=self.is_vcluster,
            resource_id=resource_id,
        )


class NamespacedResourceProxy[
    ModelT: ResourceModel,
    ListModelT: ListModel,
    DeleteModelT: ListModel | ResourceModel,
    OriginT,
](
    BaseProxy[OriginT],
):
    async def get(self, name: str) -> ModelT:
        origin = cast(
            NamespacedResource[ModelT, ListModelT, DeleteModelT], self._origin
        )
        return await origin.get(name=name, namespace=self._namespace)

    async def get_list(
        self,
        label_selector: str | None = None,
        field_selector: str | None = None,
    ) -> ListModelT:
        origin = cast(
            NamespacedResource[ModelT, ListModelT, DeleteModelT], self._origin
        )
        return await origin.get_list(
            label_selector=label_selector,
            field_selector=field_selector,
            namespace=self._namespace,
        )

    def watch(
        self,
        label_selector: str | None = None,
        resource_version: str | None = None,
        allow_watch_bookmarks: bool = False,
    ) -> Watch[ModelT]:
        origin = cast(
            NamespacedResource[ModelT, ListModelT, DeleteModelT], self._origin
        )
        return origin.watch(
            label_selector=label_selector,
            resource_version=resource_version,
            allow_watch_bookmarks=allow_watch_bookmarks,
            namespace=self._namespace,
        )

    async def create(self, model: ModelT) -> ModelT:
        origin = cast(
            NamespacedResource[ModelT, ListModelT, DeleteModelT], self._origin
        )
        return await origin.create(model=model, namespace=self._namespace)

    async def delete(
        self,
        name: str,
        *,
        payload: JsonType | None = None,
    ) -> DeleteModelT:
        origin = cast(
            NamespacedResource[ModelT, ListModelT, DeleteModelT], self._origin
        )
        return await origin.delete(
            name=name, namespace=self._namespace, payload=payload
        )

    async def get_or_create(self, model: ModelT) -> tuple[bool, ModelT]:
        origin = cast(
            NamespacedResource[ModelT, ListModelT, DeleteModelT], self._origin
        )
        return await origin.get_or_create(model=model, namespace=self._namespace)

    async def create_or_update(self, model: ModelT) -> tuple[bool, ModelT]:
        origin = cast(
            NamespacedResource[ModelT, ListModelT, DeleteModelT], self._origin
        )
        return await origin.create_or_update(model=model, namespace=self._namespace)

    async def update(self, model: ModelT) -> ModelT:
        origin = cast(
            NamespacedResource[ModelT, ListModelT, DeleteModelT], self._origin
        )
        return await origin.update(model=model, namespace=self._namespace)

    async def patch_json(
        self,
        name: str,
        patch_json_list: list[dict[str, str | Collection[str]]],
    ) -> ModelT:
        origin = cast(
            NamespacedResource[ModelT, ListModelT, DeleteModelT], self._origin
        )
        return await origin.patch_json(
            name=name, patch_json_list=patch_json_list, namespace=self._namespace
        )


class NestedResourceProxy[
    ModelT: ResourceModel,
    OriginT,
]:
    def __init__(
        self,
        origin: OriginT,
        namespace: str,
        *,
        is_vcluster: bool,
        resource_id: str | None = None,
    ):
        self.is_vcluster = is_vcluster
        self._origin = origin
        self._namespace = namespace  # 'default' for vcluster projects
        self._resource_id = resource_id

    async def get(self) -> ModelT:
        origin = cast(NestedResource[ModelT], self._origin)
        return await origin.get(self._namespace)

    async def update(self, model: ModelT) -> ModelT:
        origin = cast(NestedResource[ModelT], self._origin)
        return await origin.update(model, self._namespace)
