from collections.abc import Callable
from typing import Any, Self, overload

from ._resource_proxy import BaseProxy

type FuncT[SelfT, OriginT] = Callable[[SelfT], OriginT]


class _AttrProxy[SelfT, AttrT, OriginT]:
    def __init__(self, cls: type[AttrT], func: FuncT[SelfT, OriginT]) -> None:
        self.cls = cls
        self.func = func
        self.name: str | None = None

    def __set_name__(self, owner: BaseProxy[OriginT], name: str) -> None:
        self.name = name

    @overload
    def __get__(
        self, inst: SelfT, owner: type[BaseProxy[Any]] | None = None
    ) -> AttrT: ...
    @overload
    def __get__(
        self, inst: None, owner: type[BaseProxy[Any]] | None = None
    ) -> Self: ...
    def __get__(
        self, inst: SelfT | None, owner: type[BaseProxy[Any]] | None = None
    ) -> AttrT | Self:
        if inst is not None:
            name = self.name
            assert name is not None
            origin = self.func(inst)
            assert isinstance(inst, BaseProxy)
            namespace = inst._namespace
            ret = self.cls(origin, namespace)  # type: ignore[call-arg]
            setattr(inst, name, ret)
            return ret
        else:
            return self


type InnerT[SelfT, AttrT, OriginT] = Callable[
    [FuncT[SelfT, OriginT]], _AttrProxy[SelfT, AttrT, OriginT]
]


def attr[AttrT, SelfT: BaseProxy[Any], OriginT](
    cls: type[AttrT],
) -> InnerT[SelfT, AttrT, OriginT]:
    def inner(func: FuncT[SelfT, OriginT]) -> _AttrProxy[SelfT, AttrT, OriginT]:
        return _AttrProxy(cls, func)

    return inner
