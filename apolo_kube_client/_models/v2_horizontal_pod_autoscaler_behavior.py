from pydantic import AliasChoices, BaseModel, Field
from .v2_hpa_scaling_rules import V2HPAScalingRules

__all__ = ("V2HorizontalPodAutoscalerBehavior",)


class V2HorizontalPodAutoscalerBehavior(BaseModel):
    scale_down: V2HPAScalingRules = Field(
        default_factory=lambda: V2HPAScalingRules(),
        serialization_alias="scaleDown",
        validation_alias=AliasChoices("scale_down", "scaleDown"),
    )

    scale_up: V2HPAScalingRules = Field(
        default_factory=lambda: V2HPAScalingRules(),
        serialization_alias="scaleUp",
        validation_alias=AliasChoices("scale_up", "scaleUp"),
    )
