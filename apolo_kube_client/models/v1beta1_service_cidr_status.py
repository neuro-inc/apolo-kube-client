from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_condition import V1Condition

__all__ = ("V1beta1ServiceCIDRStatus",)


class V1beta1ServiceCIDRStatus(BaseModel):
    conditions: list[V1Condition] = Field(
        default_factory=lambda: [], alias="conditions"
    )
