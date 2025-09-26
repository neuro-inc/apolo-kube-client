from typing import Protocol, Self, overload

from ._core import _KubeCore


class _HasCore(Protocol):
    _core: _KubeCore


class _Attr[T]:
    def __init__[Args](self, cls: type[T], *args: Args) -> None:
        self.cls = cls
        self._args = args
        self.name: str | None = None

    def __set_name__(self, owner: _HasCore, name: str) -> None:
        self.name = name

    @overload
    def __get__(self, inst: _HasCore, owner: type[_HasCore] | None = None) -> T: ...
    @overload
    def __get__(self, inst: None, owner: type[_HasCore] | None = None) -> Self: ...
    def __get__(
        self, inst: _HasCore | None, owner: type[_HasCore] | None = None
    ) -> T | Self:
        if inst is not None:
            name = self.name
            assert name is not None
            ret = self.cls(inst._core, *self._args)  # type: ignore[call-arg]
            setattr(inst, name, ret)
            return ret
        else:
            return self
