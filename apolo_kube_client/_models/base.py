from typing import Any, Callable
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_list_meta import V1ListMeta


class ResourceModel(BaseModel):
    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())


class ListModel(BaseModel):
    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())


def _default_if_none[T](type_: type[T]) -> Callable[[Any], Any]:
    def validator(arg: Any) -> Any:
        if arg is None:
            return type_()
        else:
            return arg

    return validator
