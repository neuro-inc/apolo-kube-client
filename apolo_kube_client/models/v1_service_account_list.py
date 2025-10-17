from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1_service_account import V1ServiceAccount

__all__ = ("V1ServiceAccountList",)


class V1ServiceAccountList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1ServiceAccount] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
