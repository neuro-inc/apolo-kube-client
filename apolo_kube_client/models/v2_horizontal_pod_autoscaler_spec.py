from __future__ import annotations
from pydantic import BaseModel, Field
from .v2_cross_version_object_reference import V2CrossVersionObjectReference
from .v2_horizontal_pod_autoscaler_behavior import V2HorizontalPodAutoscalerBehavior
from .v2_metric_spec import V2MetricSpec

__all__ = ("V2HorizontalPodAutoscalerSpec",)


class V2HorizontalPodAutoscalerSpec(BaseModel):
    behavior: V2HorizontalPodAutoscalerBehavior = Field(
        default_factory=lambda: V2HorizontalPodAutoscalerBehavior(), alias="behavior"
    )

    max_replicas: int | None = Field(default_factory=lambda: None, alias="maxReplicas")

    metrics: list[V2MetricSpec] = Field(default_factory=lambda: [], alias="metrics")

    min_replicas: int | None = Field(default_factory=lambda: None, alias="minReplicas")

    scale_target_ref: V2CrossVersionObjectReference = Field(
        default_factory=lambda: V2CrossVersionObjectReference(), alias="scaleTargetRef"
    )
