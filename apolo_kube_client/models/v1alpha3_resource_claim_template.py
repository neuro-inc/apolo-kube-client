from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1alpha3_resource_claim_template_spec import V1alpha3ResourceClaimTemplateSpec

__all__ = ("V1alpha3ResourceClaimTemplate",)


class V1alpha3ResourceClaimTemplate(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1alpha3ResourceClaimTemplateSpec | None = Field(None, alias="spec")
