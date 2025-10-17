from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_resource_claim_template_spec import V1ResourceClaimTemplateSpec

__all__ = ("V1ResourceClaimTemplate",)


class V1ResourceClaimTemplate(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1ResourceClaimTemplateSpec = Field(
        default_factory=lambda: V1ResourceClaimTemplateSpec()
    )
