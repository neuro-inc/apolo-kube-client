from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1_service_account import V1ServiceAccount

__all__ = ("V1ServiceAccountList",)


class V1ServiceAccountList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1ServiceAccount] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
