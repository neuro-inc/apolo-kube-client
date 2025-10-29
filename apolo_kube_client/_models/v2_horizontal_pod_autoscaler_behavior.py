from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v2_hpa_scaling_rules import V2HPAScalingRules
from pydantic import BeforeValidator

__all__ = ("V2HorizontalPodAutoscalerBehavior",)


class V2HorizontalPodAutoscalerBehavior(BaseModel):
    """HorizontalPodAutoscalerBehavior configures the scaling behavior of the target in both Up and Down directions (scaleUp and scaleDown fields respectively)."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.autoscaling.v2.HorizontalPodAutoscalerBehavior"
    )

    scale_down: Annotated[
        V2HPAScalingRules,
        Field(
            alias="scaleDown",
            description="""scaleDown is scaling policy for scaling Down. If not set, the default value is to allow to scale down to minReplicas pods, with a 300 second stabilization window (i.e., the highest recommendation for the last 300sec is used).""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V2HPAScalingRules)),
    ] = V2HPAScalingRules()

    scale_up: Annotated[
        V2HPAScalingRules,
        Field(
            alias="scaleUp",
            description="""scaleUp is scaling policy for scaling Up. If not set, the default value is the higher of:
  * increase no more than 4 pods per 60 seconds
  * double the number of pods per 60 seconds
No stabilization is used.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V2HPAScalingRules)),
    ] = V2HPAScalingRules()
