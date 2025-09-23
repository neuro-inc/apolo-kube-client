from collections.abc import Collection

from .._base_resource import BaseResource, KubeResourceModel, NamespacedResource
from .._core import _KubeCore
from .._watch import Watch


class ProjectResource[
    ModelT: KubeResourceModel,
    ListModelT: KubeResourceModel,
    DeleteModelT: KubeResourceModel,
    OriginT: NamespacedResource,
](BaseResource[ModelT, ListModelT, DeleteModelT]):
    def __init__(
        self,
        core: _KubeCore,
        group_api_query_path: str,
        namespace: str,
    ):
        self._origin: OriginT = OriginT(core)
        self._namespace = namespace  # 'default' for vcluster projects

    @property
    def origin(self) -> OriginT:
        return self._origin

    async def get(self, name: str) -> ModelT:
        return await self._origin.get(name=name, namespace=self._namespace)

    async def get_list(
        self,
        label_selector: str | None = None,
    ) -> ListModelT:
        return await self._origin.get_list(
            label_selector=label_selector, namespace=self._namespace
        )

    def watch(
        self,
        label_selector: str | None = None,
        resource_version: str | None = None,
        allow_watch_bookmarks: bool = False,
    ) -> Watch[ModelT]:
        return self._origin.watch(
            label_selector=label_selector,
            resource_version=resource_version,
            allow_watch_bookmarks=allow_watch_bookmarks,
            namespace=self._namespace,
        )

    async def create(self, model: ModelT) -> ModelT:
        return await self._origin.create(model=model, namespace=self._namespace)

    async def delete(self, name: str) -> DeleteModelT:
        return await self._origin.delete(name=name, namespace=self._namespace)

    async def get_or_create(self, model: ModelT) -> tuple[bool, ModelT]:
        return await self._origin.get_or_create(model=model, namespace=self._namespace)

    async def create_or_update(self, model: ModelT) -> tuple[bool, ModelT]:
        return await self._origin.create_or_update(
            model=model, namespace=self._namespace
        )

    async def patch_json(
        self,
        name: str,
        patch_json_list: list[dict[str, str | Collection[str]]],
    ) -> ModelT:
        return await self._origin.patch_json(
            name=name, patch_json_list=patch_json_list, namespace=self._namespace
        )
