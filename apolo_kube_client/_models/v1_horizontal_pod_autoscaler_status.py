from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if
from datetime import datetime

__all__ = ("V1HorizontalPodAutoscalerStatus",)


class V1HorizontalPodAutoscalerStatus(BaseModel):
    current_cpu_utilization_percentage: int | None = Field(
        default=None,
        serialization_alias="currentCPUUtilizationPercentage",
        validation_alias=AliasChoices(
            "current_cpu_utilization_percentage", "currentCPUUtilizationPercentage"
        ),
        exclude_if=_exclude_if,
    )

    current_replicas: int | None = Field(
        default=None,
        serialization_alias="currentReplicas",
        validation_alias=AliasChoices("current_replicas", "currentReplicas"),
        exclude_if=_exclude_if,
    )

    desired_replicas: int | None = Field(
        default=None,
        serialization_alias="desiredReplicas",
        validation_alias=AliasChoices("desired_replicas", "desiredReplicas"),
        exclude_if=_exclude_if,
    )

    last_scale_time: datetime | None = Field(
        default=None,
        serialization_alias="lastScaleTime",
        validation_alias=AliasChoices("last_scale_time", "lastScaleTime"),
        exclude_if=_exclude_if,
    )

    observed_generation: int | None = Field(
        default=None,
        serialization_alias="observedGeneration",
        validation_alias=AliasChoices("observed_generation", "observedGeneration"),
        exclude_if=_exclude_if,
    )
