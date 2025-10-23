from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v2_hpa_scaling_rules import V2HPAScalingRules
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V2HorizontalPodAutoscalerBehavior",)


class V2HorizontalPodAutoscalerBehavior(BaseModel):
    scale_down: Annotated[
        V2HPAScalingRules, BeforeValidator(_default_if_none(V2HPAScalingRules))
    ] = Field(
        default_factory=lambda: V2HPAScalingRules(),
        serialization_alias="scaleDown",
        validation_alias=AliasChoices("scale_down", "scaleDown"),
        exclude_if=_exclude_if,
    )

    scale_up: Annotated[
        V2HPAScalingRules, BeforeValidator(_default_if_none(V2HPAScalingRules))
    ] = Field(
        default_factory=lambda: V2HPAScalingRules(),
        serialization_alias="scaleUp",
        validation_alias=AliasChoices("scale_up", "scaleUp"),
        exclude_if=_exclude_if,
    )
