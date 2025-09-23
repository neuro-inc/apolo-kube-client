from typing import Protocol, overload

from ._core import _KubeCore


class _HasCore(Protocol):
    _core: _KubeCore


class _Attr[T]:
    def __init__[Args](self, cls: type[T], *args: Args) -> None:
        self._cls = cls
        self._args = args
        self._name: str | None = None

    def __set_name__(self, owner: _HasCore, name: str) -> None:
        self._name = name

    @overload
    def __get__(self, inst: _HasCore, owner: type[_HasCore] | None = None) -> T: ...
    @overload
    def __get__(self, inst: None, owner: type[_HasCore] | None = None) -> type[T]: ...
    def __get__(
        self, inst: _HasCore | None, owner: type[_HasCore] | None = None
    ) -> T | type[T]:
        if inst is not None:
            name = self._name
            assert name is not None
            ret = self._cls(inst._core, *self._args)
            setattr(inst, name, ret)
            return ret
        else:
            return self._cls
