from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_lease import V1Lease
from .v1_list_meta import V1ListMeta

__all__ = ("V1LeaseList",)


class V1LeaseList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1Lease] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
