from __future__ import annotations

import asyncio
import logging
from collections import defaultdict
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from dataclasses import dataclass
from types import TracebackType
from typing import Self

from cachetools import LRUCache
from kubernetes.client.models import V1Secret

from apolo_kube_client._client import KubeClient
from apolo_kube_client._config import KubeConfig
from apolo_kube_client._errors import ResourceNotFound
from apolo_kube_client._transport import KubeTransport
from apolo_kube_client._vcluster._cache import AsyncLRUCache
from apolo_kube_client._vcluster._client_factory import (
    VclusterClientFactory,
)
from apolo_kube_client._vcluster._client_proxy import KubeClientProxy
from apolo_kube_client.apolo import create_namespace, generate_namespace_name

logger = logging.getLogger(__name__)


class KubeClientSelectorError(Exception):
    """Base selector error"""


class CloseInProgressError(KubeClientSelectorError):
    """Raised when selector is closing"""


@dataclass
class VclusterEntry:
    client: KubeClient
    leases: int = 0  # active context leases


class KubeClientSelector:
    """

    Example usage:

    >>> async def main():
    >>>     kube_config = KubeConfig(...)
    >>>
    >>>     async with KubeClientSelector(
    >>>         config=kube_config
    >>>     ) as selector:
    >>>         async with selector.get_client(org_name=..., project_name=...) as k8s:
    >>>             namespaces = await k8s.core_v1.namespace.get_list()
    """

    DEFAULT_VCLUSTER_CACHE_SIZE: int = 32
    DEFAULT_REAL_CLUSTER_CACHE_SIZE: int = 1024

    _VCLUSTER_SECRET_PREFIX = "vc"

    def __init__(
        self,
        *,
        config: KubeConfig,
        vcluster_cache_size: int = DEFAULT_VCLUSTER_CACHE_SIZE,
        real_cluster_cache_size: int = DEFAULT_REAL_CLUSTER_CACHE_SIZE,
    ) -> None:
        self._config = config
        # we pre-create a dedicated kube transport,
        # since we already know that we'll work in a multi-cluster mode
        self._transport = KubeTransport(
            conn_pool_size=config.client_conn_pool_size,
            conn_timeout_s=config.client_conn_timeout_s,
            read_timeout_s=config.client_read_timeout_s,
        )
        # create a host client that'll be used to access to a host kube cluster
        self._host_client = KubeClient(config=config, transport=self._transport)
        self._vcluster_client_factory = VclusterClientFactory(
            default_config=config,
            transport=self._transport,
        )
        self._locks: dict[str, asyncio.Lock] = defaultdict(asyncio.Lock)

        # cache of a "default" client.
        # if we are confident that a particular org+project uses a host kube
        # client - there is no need to fetch a vcluster secret.
        self._host_cache: LRUCache[str, bool] = LRUCache(
            maxsize=real_cluster_cache_size
        )

        self._vcluster_cache = AsyncLRUCache[str, VclusterEntry](
            maxsize=vcluster_cache_size,
            on_evict=self._on_vcluster_evict,
        )
        # zombies are possible if LRU cache is already overwhelmed,
        # but request that uses a zombie kube client is not yet finished
        self._vcluster_zombies: dict[str, VclusterEntry] = {}
        self._closing = False

    async def __aenter__(self) -> Self:
        logger.info(f"{self}: initializing...")
        await self._transport.__aenter__()
        await self._host_client.__aenter__()
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.aclose()

    async def aclose(self) -> None:
        logger.info(f"{self}: closing...")
        if self._closing:
            return
        self._closing = True

        logger.info(f"{self}: evicting all vcluster cached entries")
        await self._vcluster_cache.close()

        logger.info(f"{self}: closing zombies")
        for key, entry in list(self._vcluster_zombies.items()):
            await self._vcluster_client_factory.close(client=entry.client)
            self._vcluster_zombies.pop(key, None)

        # Close the shared default client, and a common transport
        logger.info(f"{self}: closing default client")
        await self._host_client.__aexit__(None, None, None)
        logger.info(f"{self}: closing transport")
        await self._transport.__aexit__(None, None, None)

    @property
    def host_client(self) -> KubeClient:
        """Return a kube client instance connected to the host kubernetes"""
        return self._host_client

    @asynccontextmanager
    async def get_client(
        self,
        *,
        org_name: str,
        project_name: str,
    ) -> AsyncIterator[KubeClientProxy]:
        """
        Client acquisition entry-point.
        Resolution order:
        1. vcluster cache hit: lease and return.
        2. host client cache hit: return shared client.
        3. fetch secret:
           - found: build vcluster client, cache, lease, return.
           - not found: return shared host client.

        Resolution happens under the per-project lock to avoid fetching
        vcluster secret multiple times.
        A client is yielded without the lock, so concurrent usage is possible.

        If client was resolved to a host one, a selector wil automatically
        create a namespace under the hood.
        """
        if self._closing:
            raise CloseInProgressError()

        namespace = cache_key = generate_namespace_name(org_name, project_name)

        entry: VclusterEntry | None = None
        client: KubeClient

        async with self._locks[cache_key]:
            cached = self._vcluster_cache.get(cache_key)
            if cached is not None:
                logger.info(f"{self}: vcluster cache hit: lease and return")
                cached.leases += 1
                entry = cached
                client = cached.client
                namespace = "default"
            elif self._is_host_client(cache_key):
                logger.info(f"{self}: host client cache hit: return host client")
                client = self._host_client
            else:
                # Try to fetch secret
                secret_name = f"{self._VCLUSTER_SECRET_PREFIX}-{namespace}"
                secret = await self._fetch_vcluster_secret(
                    secret_name=secret_name,
                    namespace=namespace,
                )
                if secret:
                    logger.info(
                        f"{self}: secret found: "
                        f"build vcluster client, cache, lease, return"
                    )
                    client = await self._vcluster_client_factory.from_secret(secret)
                    entry = VclusterEntry(client=client, leases=1)
                    await self._vcluster_cache.set(cache_key, entry)
                    namespace = "default"
                else:
                    logger.info(f"{self}: secret not found: return shared host client")
                    self._host_cache[cache_key] = True
                    client = self._host_client
                    # ensure namespace is in place
                    await create_namespace(client, org_name, project_name)

        try:
            yield KubeClientProxy(client, namespace)
        finally:
            await self._release_vcluster_lease(cache_key, entry)

    async def _release_vcluster_lease(
        self, key: str, entry: VclusterEntry | None
    ) -> None:
        if not entry:
            return None
        entry.leases -= 1
        if entry.leases <= 0 and key in self._vcluster_zombies:
            self._vcluster_zombies.pop(key, None)
            await self._vcluster_client_factory.close(client=entry.client)

    def _is_host_client(self, namespace: str) -> bool:
        try:
            # For cachetools.LRUCache, __contains__ doesn't update recency.
            # A safe way to 'touch' on read is to try __getitem__.
            _ = self._host_cache[namespace]
            return True
        except KeyError:
            return False

    async def _fetch_vcluster_secret(
        self,
        *,
        secret_name: str,
        namespace: str,
    ) -> V1Secret | None:
        try:
            return await self._host_client.core_v1.secret.get(
                name=secret_name, namespace=namespace
            )
        except ResourceNotFound:
            return None

    async def _on_vcluster_evict(self, key: str, entry: VclusterEntry) -> None:
        if entry.leases <= 0:
            # close immediately
            await self._vcluster_client_factory.close(client=entry.client)
        else:
            # some concurrent request is still using it. let's mark as zombie
            self._vcluster_zombies[key] = entry
