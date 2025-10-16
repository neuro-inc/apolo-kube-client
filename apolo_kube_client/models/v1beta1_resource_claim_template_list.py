from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1beta1_resource_claim_template import V1beta1ResourceClaimTemplate

__all__ = ("V1beta1ResourceClaimTemplateList",)


class V1beta1ResourceClaimTemplateList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1beta1ResourceClaimTemplate] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
