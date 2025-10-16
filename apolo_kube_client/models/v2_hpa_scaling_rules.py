from __future__ import annotations
from pydantic import BaseModel, Field
from .v2_hpa_scaling_policy import V2HPAScalingPolicy

__all__ = ("V2HPAScalingRules",)


class V2HPAScalingRules(BaseModel):
    policies: list[V2HPAScalingPolicy] = Field(
        default_factory=lambda: [], alias="policies"
    )

    select_policy: str | None = Field(
        default_factory=lambda: None, alias="selectPolicy"
    )

    stabilization_window_seconds: int | None = Field(
        default_factory=lambda: None, alias="stabilizationWindowSeconds"
    )

    tolerance: str | None = Field(default_factory=lambda: None, alias="tolerance")
