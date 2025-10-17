from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_api_service import V1APIService
from .v1_list_meta import V1ListMeta

__all__ = ("V1APIServiceList",)


class V1APIServiceList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1APIService] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
