from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1PodResourceClaimStatus",)


class V1PodResourceClaimStatus(BaseModel):
    name: str | None = Field(default_factory=lambda: None)

    resource_claim_name: str | None = Field(
        default_factory=lambda: None, alias="resourceClaimName"
    )
