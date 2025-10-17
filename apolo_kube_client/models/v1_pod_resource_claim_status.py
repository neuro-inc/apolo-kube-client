from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1PodResourceClaimStatus",)


class V1PodResourceClaimStatus(BaseModel):
    name: str | None = Field(default=None)

    resource_claim_name: str | None = Field(
        default=None,
        serialization_alias="resourceClaimName",
        validation_alias=AliasChoices("resource_claim_name", "resourceClaimName"),
    )
