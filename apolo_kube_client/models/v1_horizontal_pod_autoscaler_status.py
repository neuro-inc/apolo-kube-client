from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

__all__ = ("V1HorizontalPodAutoscalerStatus",)


class V1HorizontalPodAutoscalerStatus(BaseModel):
    current_cpu_utilization_percentage: int | None = Field(
        None, alias="currentCPUUtilizationPercentage"
    )

    current_replicas: int | None = Field(None, alias="currentReplicas")

    desired_replicas: int | None = Field(None, alias="desiredReplicas")

    last_scale_time: datetime | None = Field(None, alias="lastScaleTime")

    observed_generation: int | None = Field(None, alias="observedGeneration")
