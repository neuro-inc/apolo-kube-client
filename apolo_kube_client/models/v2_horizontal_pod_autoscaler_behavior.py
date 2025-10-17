from __future__ import annotations
from pydantic import BaseModel, Field
from .v2_hpa_scaling_rules import V2HPAScalingRules

__all__ = ("V2HorizontalPodAutoscalerBehavior",)


class V2HorizontalPodAutoscalerBehavior(BaseModel):
    scale_down: V2HPAScalingRules = Field(
        default_factory=lambda: V2HPAScalingRules(), alias="scaleDown"
    )

    scale_up: V2HPAScalingRules = Field(
        default_factory=lambda: V2HPAScalingRules(), alias="scaleUp"
    )
