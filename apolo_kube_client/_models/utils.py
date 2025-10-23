from typing import Any, Callable
from pydantic import BaseModel


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
        return v.model_dump() == v.__class__().model_dump()
    if isinstance(v, (list, dict)):
        return not v
    return False
