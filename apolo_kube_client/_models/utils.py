from collections.abc import Callable
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class KubeMeta:
    group: str
    kind: str
    version: str


def _default_if_none[T](type_: type[T]) -> Callable[[Any], Any]:
    def validator(arg: Any) -> Any:
        if arg is None:
            return type_()
        return arg

    return validator


def _collection_if_none(type_: str) -> Callable[[Any], Any]:
    def validator(arg: Any) -> Any:
        if arg is None:
            return eval(type_)
        return arg

    return validator
