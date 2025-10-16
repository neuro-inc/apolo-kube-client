from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ("V1HorizontalPodAutoscalerStatus",)


class V1HorizontalPodAutoscalerStatus(BaseModel):
    current_cpu_utilization_percentage: int | None = Field(
        default_factory=lambda: None, alias="currentCPUUtilizationPercentage"
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
