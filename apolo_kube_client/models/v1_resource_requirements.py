from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_resource_claim import V1ResourceClaim

__all__ = ("V1ResourceRequirements",)


class V1ResourceRequirements(BaseModel):
    claims: list[V1ResourceClaim] | None = Field(None, alias="claims")

    limits: dict[str, str] | None = Field(None, alias="limits")

    requests: dict[str, str] | None = Field(None, alias="requests")
