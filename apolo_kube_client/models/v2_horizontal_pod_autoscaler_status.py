from __future__ import annotations
from pydantic import BaseModel, Field
from .v2_horizontal_pod_autoscaler_condition import V2HorizontalPodAutoscalerCondition
from .v2_metric_status import V2MetricStatus
from datetime import datetime

__all__ = ("V2HorizontalPodAutoscalerStatus",)


class V2HorizontalPodAutoscalerStatus(BaseModel):
    conditions: list[V2HorizontalPodAutoscalerCondition] = Field(
        default_factory=lambda: []
    )

    current_metrics: list[V2MetricStatus] = Field(
        default_factory=lambda: [], alias="currentMetrics"
    )

    current_replicas: int | None = Field(
        default_factory=lambda: None, alias="currentReplicas"
    )

    desired_replicas: int | None = Field(
        default_factory=lambda: None, alias="desiredReplicas"
    )

    last_scale_time: datetime | None = Field(
        default_factory=lambda: None, alias="lastScaleTime"
    )

    observed_generation: int | None = Field(
        default_factory=lambda: None, alias="observedGeneration"
    )
