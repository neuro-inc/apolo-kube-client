from __future__ import annotations

from collections import OrderedDict
from collections.abc import Awaitable, Callable
from typing import TypeVar

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
        try:
            v = self._data[key]
        except KeyError:
            return None
        # Move key to MRU
        self._data.move_to_end(key, last=True)
        return v

    async def set(self, key: K, value: V) -> None:
        # Insert/update and move to MRU
        self._data[key] = value
        self._data.move_to_end(key, last=True)
        while len(self._data) > self._maxsize:
            old_key, old_val = self._data.popitem(last=False)  # LRU
            await self._on_evict(old_key, old_val)

    async def close(self) -> None:
        while self._data:
            k, v = self._data.popitem(last=False)
            await self._on_evict(k, v)
