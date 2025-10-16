from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1_resource_quota import V1ResourceQuota

__all__ = ("V1ResourceQuotaList",)


class V1ResourceQuotaList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1ResourceQuota] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
