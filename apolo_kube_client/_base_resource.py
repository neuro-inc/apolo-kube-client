from typing import Any

from yarl import URL

from apolo_kube_client._core import _KubeCore


class BaseResource:
    """
    Base class for Non Namespaced Kubernetes Resource.
    """

    query_path: str
    model: str
    list_model: str

    def __init__(self, core: _KubeCore, group_api_query_path: str):
        if not self.query_path:
            raise ValueError("resource api query_path must be set")

        self._core: _KubeCore = core
        self._group_api_query_path: str = group_api_query_path

    def _build_url_list(self, *args: Any, **kwargs: Any) -> URL:
        raise NotImplementedError

    def _build_url(self, *args: Any, **kwargs: Any) -> URL:
        raise NotImplementedError

    async def get(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError

    async def list(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError

    async def create(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError

    async def delete(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError


class ClusterScopedResource(BaseResource):
    def _build_url_list(self) -> URL:
        assert self.query_path, "query_path must be set"
        return self._core.base_url / self._group_api_query_path / self.query_path

    def _build_url(self, name: str) -> URL:
        return self._build_url_list() / name

    async def get(self, name: str) -> Any:
        return await self._core.get(url=self._build_url(name), response_type=self.model)

    async def list(self) -> Any:
        return await self._core.get(
            url=self._build_url_list(), response_type=self.list_model
        )

    async def create(self, model: Any) -> Any:
        return await self._core.post(
            url=self._build_url_list(), json=model.to_dict(), response_type=self.model
        )

    async def delete(self, name: str) -> Any:
        return await self._core.get(url=self._build_url(name), response_type=self.model)


class NamespacedResource(BaseResource):
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

    async def get(self, name: str, namespace: str | None = None) -> Any:
        return await self._core.get(
            url=self._build_url(name, self._get_ns(namespace)), response_type=self.model
        )

    async def list(self, namespace: str | None = None) -> Any:
        return await self._core.get(
            url=self._build_url_list(self._get_ns(namespace)),
            response_type=self.list_model,
        )

    async def create(self, model: Any, namespace: str | None = None) -> Any:
        return await self._core.post(
            url=self._build_url_list(self._get_ns(namespace)),
            json=model.to_dict(),
            response_type=self.model,
        )

    async def delete(self, name: str, namespace: str | None = None) -> Any:
        return await self._core.get(
            url=self._build_url(name, self._get_ns(namespace)), response_type=self.model
        )
