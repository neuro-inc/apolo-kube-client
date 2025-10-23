from dataclasses import dataclass
from typing import Any, Callable
from pydantic import BaseModel


@dataclass(frozen=True)
class KubeMeta:
    group: str
    kind: str
    version: str


def _default_if_none[T](type_: type[T]) -> Callable[[Any], Any]:
    def validator(arg: Any) -> Any:
        if arg is None:
            return type_()
        else:
            return arg

    return validator


def _collection_if_none(type_: str) -> Callable[[Any], Any]:
    def validator(arg: Any) -> Any:
        if arg is None:
            return eval(type_)
        else:
            return arg

    return validator


def _exclude_if(v: Any) -> bool:
    if v is None:
        return True
    if isinstance(v, BaseModel):
        type_ = type(v)
        required = any(f.is_required() for f in type_.model_fields.values())
        if required:
            return False
        return v.model_dump() == type_().model_dump()
    if isinstance(v, (list, dict)):
        return not v
    return False
