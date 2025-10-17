from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1beta2_resource_claim_template import V1beta2ResourceClaimTemplate

__all__ = ("V1beta2ResourceClaimTemplateList",)


class V1beta2ResourceClaimTemplateList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[V1beta2ResourceClaimTemplate] = Field(default_factory=lambda: [])

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
