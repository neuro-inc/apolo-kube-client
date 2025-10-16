from __future__ import annotations
from pydantic import BaseModel, Field
from .core_v1_resource_claim import CoreV1ResourceClaim

__all__ = ("V1ResourceRequirements",)


class V1ResourceRequirements(BaseModel):
    claims: list[CoreV1ResourceClaim] = Field(
        default_factory=lambda: [], alias="claims"
    )

    limits: dict[str, str] = Field(default_factory=lambda: {}, alias="limits")

    requests: dict[str, str] = Field(default_factory=lambda: {}, alias="requests")
