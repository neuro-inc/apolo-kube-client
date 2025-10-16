from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_cross_version_object_reference import V1CrossVersionObjectReference

__all__ = ("V1HorizontalPodAutoscalerSpec",)


class V1HorizontalPodAutoscalerSpec(BaseModel):
    max_replicas: int | None = Field(default_factory=lambda: None, alias="maxReplicas")

    min_replicas: int | None = Field(default_factory=lambda: None, alias="minReplicas")

    scale_target_ref: V1CrossVersionObjectReference = Field(
        default_factory=lambda: V1CrossVersionObjectReference(), alias="scaleTargetRef"
    )

    target_cpu_utilization_percentage: int | None = Field(
        default_factory=lambda: None, alias="targetCPUUtilizationPercentage"
    )
