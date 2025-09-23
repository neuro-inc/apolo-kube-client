from __future__ import annotations

from collections import OrderedDict
from collections.abc import Awaitable
from typing import Callable, Generic, Optional, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class AsyncLRUCache[K, V]:
    def __init__(
        self,
        maxsize: int,
        on_evict: Callable[[K, V], Awaitable[None]],
    ) -> None:
        self._maxsize = maxsize
        self._data: OrderedDict[K, V] = OrderedDict()
        self._on_evict = on_evict

    def __len__(self) -> int:
        return len(self._data)

    def get(self, key: K) -> V | None:
        if key not in self._data:
            return None
        v = self._data.pop(key)
        self._data[key] = v  # move to MRU
        return v

    async def set(self, key: K, value: V) -> None:
        if key in self._data:
            self._data.pop(key)
        self._data[key] = value
        while len(self._data) > self._maxsize:
            old_key, old_val = self._data.popitem(last=False)  # LRU
            await self._on_evict(old_key, old_val)

    async def close(self) -> None:
        while self._data:
            k, v = self._data.popitem(last=False)
            await self._on_evict(k, v)
