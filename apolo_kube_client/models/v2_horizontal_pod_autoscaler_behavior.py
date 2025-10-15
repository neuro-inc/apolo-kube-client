from pydantic import BaseModel, Field

from .v2_h_p_a_scaling_rules import V2HPAScalingRules


class V2HorizontalPodAutoscalerBehavior(BaseModel):
    scale_down: V2HPAScalingRules | None = Field(None, alias="scaleDown")

    scale_up: V2HPAScalingRules | None = Field(None, alias="scaleUp")
