from __future__ import annotations
from pydantic import BaseModel, Field
from .resource_v1_resource_claim import ResourceV1ResourceClaim
from .v1_list_meta import V1ListMeta

__all__ = ("V1ResourceClaimList",)


class V1ResourceClaimList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[ResourceV1ResourceClaim] = Field(default_factory=lambda: [])

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
