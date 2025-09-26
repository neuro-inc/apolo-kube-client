import functools
from collections.abc import Callable
from typing import Any, overload

from ._base_resource import Base


class _Attr[AttrT, OriginT]:
    def __init__(self, cls: type[AttrT], origin: OriginT, namespace: str) -> None:
        self._cls = cls
        self._origin = origin
        self._namespace = namespace
        self._name: str | None = None

    def __set_name__(self, owner: Base[OriginT], name: str) -> None:
        self._name = name

    @overload
    def __get__(
        self, inst: Base[Any], owner: type[Base[Any]] | None = None
    ) -> AttrT: ...
    @overload
    def __get__(
        self, inst: None, owner: type[Base[Any]] | None = None
    ) -> type[AttrT]: ...
    def __get__(
        self, inst: Base[Any] | None, owner: type[Base[Any]] | None = None
    ) -> AttrT | type[AttrT]:
        if inst is not None:
            name = self._name
            assert name is not None
            ret = self._cls(self._origin, self._namespace)  # type: ignore[call-arg]
            setattr(inst, name, ret)
            return ret
        else:
            return self._cls


type FuncT[SelfT, OriginT] = Callable[[SelfT], OriginT]
type WrapperT[SelfT, AttrT, OriginT] = Callable[[SelfT], _Attr[AttrT, OriginT]]
type InnerT[SelfT, AttrT, OriginT] = Callable[
    [FuncT[SelfT, OriginT]], WrapperT[SelfT, AttrT, OriginT]
]


def attr[AttrT, SelfT: Base[Any], OriginT](
    cls: type[AttrT],
) -> InnerT[SelfT, AttrT, OriginT]:
    def inner(func: FuncT[SelfT, OriginT]) -> WrapperT[SelfT, AttrT, OriginT]:
        @functools.wraps(func)
        def wrapper(self: SelfT) -> _Attr[AttrT, OriginT]:
            func(self)
            return _Attr(cls, self._origin, self._namespace)

        return wrapper

    return inner
