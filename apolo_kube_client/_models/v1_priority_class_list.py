from pydantic import AliasChoices, Field
from .base import ListModel
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_list_meta import V1ListMeta
from .v1_priority_class import V1PriorityClass
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PriorityClassList",)


class V1PriorityClassList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: Annotated[
        list[V1PriorityClass], BeforeValidator(_collection_if_none("[]"))
    ] = []

    kind: str | None = None

    metadata: Annotated[V1ListMeta, BeforeValidator(_default_if_none(V1ListMeta))] = (
        Field(default_factory=lambda: V1ListMeta())
    )
