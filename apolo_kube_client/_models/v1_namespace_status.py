from pydantic import BaseModel
from .utils import _collection_if_none
from .v1_namespace_condition import V1NamespaceCondition
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1NamespaceStatus",)


class V1NamespaceStatus(BaseModel):
    conditions: Annotated[
        list[V1NamespaceCondition], BeforeValidator(_collection_if_none("[]"))
    ] = []

    phase: str | None = None
