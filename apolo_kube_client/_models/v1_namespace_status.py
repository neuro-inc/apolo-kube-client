from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_namespace_condition import V1NamespaceCondition
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1NamespaceStatus",)


class V1NamespaceStatus(BaseModel):
    conditions: Annotated[
        list[V1NamespaceCondition], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    phase: str | None = Field(default=None, exclude_if=_exclude_if)
