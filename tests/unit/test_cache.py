from unittest.mock import AsyncMock

from apolo_kube_client._vcluster._cache import AsyncLRUCache


async def test_async_lru_evicts_in_lru_order_and_awaits_hook() -> None:
    evicted = []
    on_evict = AsyncMock(side_effect=lambda k, v: evicted.append((k, v)))
    cache = AsyncLRUCache[str, int](maxsize=2, on_evict=on_evict)

    await cache.set("a", 1)
    await cache.set("b", 2)
    # touch "a" to make "b" the LRU
    assert cache.get("a") == 1
    await cache.set("c", 3)  # should evict "b"

    assert evicted == [("b", 2)]
    on_evict.assert_awaited()


async def test_async_lru_close_calls_evict_for_all() -> None:
    evicted = []
    on_evict = AsyncMock(side_effect=lambda k, v: evicted.append(k))
    cache = AsyncLRUCache[str, int](maxsize=3, on_evict=on_evict)

    await cache.set("a", 1)
    await cache.set("b", 2)
    await cache.set("c", 3)

    await cache.close()
    assert set(evicted) == {"a", "b", "c"}


async def test_get_missing_returns_none_and_does_not_modify_order() -> None:
    evicted: list[tuple[str, int]] = []
    on_evict = AsyncMock(side_effect=lambda k, v: evicted.append((k, v)))
    cache = AsyncLRUCache[str, int](maxsize=2, on_evict=on_evict)

    await cache.set("a", 1)
    await cache.set("b", 2)

    # Getting a missing key should return None and not affect LRU order
    assert cache.get("missing") is None

    await cache.set("c", 3)  # should evict "a" (still LRU)
    assert evicted == [("a", 1)]


async def test_set_existing_updates_value_and_moves_to_mru_without_eviction() -> None:
    evicted: list[tuple[str, int]] = []
    on_evict = AsyncMock(side_effect=lambda k, v: evicted.append((k, v)))
    cache = AsyncLRUCache[str, int](maxsize=2, on_evict=on_evict)

    await cache.set("a", 1)
    await cache.set("b", 2)

    # Update existing key; should not evict and should move to MRU
    await cache.set("a", 10)
    assert evicted == []
    assert cache.get("a") == 10

    # Now inserting another key should evict "b" (LRU)
    await cache.set("c", 3)
    assert evicted == [("b", 2)]


async def test_len_reflects_current_size_and_after_eviction() -> None:
    on_evict = AsyncMock()
    cache = AsyncLRUCache[str, int](maxsize=2, on_evict=on_evict)

    assert len(cache) == 0
    await cache.set("a", 1)
    await cache.set("b", 2)
    assert len(cache) == 2

    await cache.set("c", 3)  # evicts one, but size stays at max
    assert len(cache) == 2


async def test_close_evicts_in_current_lru_order() -> None:
    order: list[tuple[str, int]] = []
    on_evict = AsyncMock(side_effect=lambda k, v: order.append((k, v)))
    cache = AsyncLRUCache[str, int](maxsize=3, on_evict=on_evict)

    await cache.set("a", 1)
    await cache.set("b", 2)
    await cache.set("c", 3)

    # Reorder to make LRU order: c (LRU), a, b (MRU)
    assert cache.get("a") == 1  # now: b, c, a
    assert cache.get("b") == 2  # now: c, a, b

    await cache.close()
    assert order == [("c", 3), ("a", 1), ("b", 2)]


async def test_set_over_capacity_triggers_sequential_evictions() -> None:
    evicted_keys: list[str] = []
    on_evict = AsyncMock(side_effect=lambda k, v: evicted_keys.append(k))
    cache = AsyncLRUCache[str, int](maxsize=1, on_evict=on_evict)

    await cache.set("a", 1)
    await cache.set("b", 2)  # evict a
    await cache.set("c", 3)  # evict b

    assert evicted_keys == ["a", "b"]
