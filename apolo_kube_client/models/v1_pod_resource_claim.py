from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1PodResourceClaim",)


class V1PodResourceClaim(BaseModel):
    name: str | None = Field(default_factory=lambda: None, alias="name")

    resource_claim_name: str | None = Field(
        default_factory=lambda: None, alias="resourceClaimName"
    )

    resource_claim_template_name: str | None = Field(
        default_factory=lambda: None, alias="resourceClaimTemplateName"
    )
