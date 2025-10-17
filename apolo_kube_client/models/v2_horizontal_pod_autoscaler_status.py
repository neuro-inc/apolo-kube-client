from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v2_horizontal_pod_autoscaler_condition import V2HorizontalPodAutoscalerCondition
from .v2_metric_status import V2MetricStatus
from datetime import datetime

__all__ = ("V2HorizontalPodAutoscalerStatus",)


class V2HorizontalPodAutoscalerStatus(BaseModel):
    conditions: list[V2HorizontalPodAutoscalerCondition] = Field(default=[])

    current_metrics: list[V2MetricStatus] = Field(
        default=[],
        serialization_alias="currentMetrics",
        validation_alias=AliasChoices("current_metrics", "currentMetrics"),
    )

    current_replicas: int | None = Field(
        default=None,
        serialization_alias="currentReplicas",
        validation_alias=AliasChoices("current_replicas", "currentReplicas"),
    )

    desired_replicas: int | None = Field(
        default=None,
        serialization_alias="desiredReplicas",
        validation_alias=AliasChoices("desired_replicas", "desiredReplicas"),
    )

    last_scale_time: datetime | None = Field(
        default=None,
        serialization_alias="lastScaleTime",
        validation_alias=AliasChoices("last_scale_time", "lastScaleTime"),
    )

    observed_generation: int | None = Field(
        default=None,
        serialization_alias="observedGeneration",
        validation_alias=AliasChoices("observed_generation", "observedGeneration"),
    )
