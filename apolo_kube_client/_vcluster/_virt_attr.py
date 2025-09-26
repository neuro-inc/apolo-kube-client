from collections.abc import Callable
from typing import Any, overload

from ._virt_base_resource import Base

type FuncT[SelfT, OriginT] = Callable[[SelfT], OriginT]


class _Attr[SelfT, AttrT, OriginT]:
    def __init__(self, cls: type[AttrT], func: FuncT[SelfT, OriginT]) -> None:
        self._cls = cls
        self._func = func
        self._name: str | None = None

    def __set_name__(self, owner: Base[OriginT], name: str) -> None:
        self._name = name

    @overload
    def __get__(self, inst: SelfT, owner: type[Base[Any]] | None = None) -> AttrT: ...
    @overload
    def __get__(
        self, inst: None, owner: type[Base[Any]] | None = None
    ) -> type[AttrT]: ...
    def __get__(
        self, inst: SelfT | None, owner: type[Base[Any]] | None = None
    ) -> AttrT | type[AttrT]:
        if inst is not None:
            name = self._name
            assert name is not None
            origin = self._func(inst)
            assert isinstance(inst, Base)
            namespace = inst._namespace
            ret = self._cls(origin, namespace)  # type: ignore[call-arg]
            setattr(inst, name, ret)
            return ret
        else:
            return self._cls


type InnerT[SelfT, AttrT, OriginT] = Callable[
    [FuncT[SelfT, OriginT]], _Attr[SelfT, AttrT, OriginT]
]


def attr[AttrT, SelfT: Base[Any], OriginT](
    cls: type[AttrT],
) -> InnerT[SelfT, AttrT, OriginT]:
    def inner(func: FuncT[SelfT, OriginT]) -> _Attr[SelfT, AttrT, OriginT]:
        return _Attr(cls, func)

    return inner
