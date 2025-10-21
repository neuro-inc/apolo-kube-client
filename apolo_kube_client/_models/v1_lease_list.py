from pydantic import AliasChoices, Field
from .base import ListModel
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_lease import V1Lease
from .v1_list_meta import V1ListMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1LeaseList",)


class V1LeaseList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: Annotated[list[V1Lease], BeforeValidator(_collection_if_none("[]"))] = []

    kind: str | None = None

    metadata: Annotated[V1ListMeta, BeforeValidator(_default_if_none(V1ListMeta))] = (
        Field(default_factory=lambda: V1ListMeta())
    )
