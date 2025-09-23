from collections.abc import Collection

from .._base_resource import BaseResource, KubeResourceModel, NamespacedResource
from .._core import _KubeCore
from .._watch import Watch
from ..apolo import generate_namespace_name


class ProjectResource[
    ModelT: KubeResourceModel,
    ListModelT: KubeResourceModel,
    DeleteModelT: KubeResourceModel,
](BaseResource[ModelT, ListModelT, DeleteModelT]):
    def __init__(
        self,
        core: _KubeCore,
        group_api_query_path: str,
        *,
        is_vcluster: bool,
        org_name: str,
        project_name: str,
    ):
        self._ns_resource: NamespacedResource[ModelT, ListModelT, DeleteModelT] = (
            NamespacedResource(core, group_api_query_path)
        )
        if is_vcluster:
            self._namespace = "default"
        else:
            self._namespace = generate_namespace_name(org_name, project_name)

    async def get_list(
        self,
        label_selector: str | None = None,
    ) -> ListModelT:
        return await self._ns_resource.get_list(
            label_selector=label_selector, namespace=self._namespace
        )

    def watch(
        self,
        label_selector: str | None = None,
        resource_version: str | None = None,
        allow_watch_bookmarks: bool = False,
    ) -> Watch[ModelT]:
        return self._ns_resource.watch(
            label_selector=label_selector,
            resource_version=resource_version,
            allow_watch_bookmarks=allow_watch_bookmarks,
            namespace=self._namespace,
        )

    async def create(self, model: ModelT) -> ModelT:
        return await self._ns_resource.create(model=model, namespace=self._namespace)

    async def delete(self, name: str) -> DeleteModelT:
        return await self._ns_resource.delete(name=name, namespace=self._namespace)

    async def get_or_create(self, model: ModelT) -> tuple[bool, ModelT]:
        return await self._ns_resource.get_or_create(
            model=model, namespace=self._namespace
        )

    async def create_or_update(self, model: ModelT) -> tuple[bool, ModelT]:
        return await self._ns_resource.create_or_update(
            model=model, namespace=self._namespace
        )

    async def patch_json(
        self,
        name: str,
        patch_json_list: list[dict[str, str | Collection[str]]],
    ) -> ModelT:
        return await self._ns_resource.patch_json(
            name=name, patch_json_list=patch_json_list, namespace=self._namespace
        )
