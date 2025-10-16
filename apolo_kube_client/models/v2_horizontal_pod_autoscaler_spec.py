from __future__ import annotations

from pydantic import BaseModel, Field

from .v2_cross_version_object_reference import V2CrossVersionObjectReference
from .v2_horizontal_pod_autoscaler_behavior import V2HorizontalPodAutoscalerBehavior
from .v2_metric_spec import V2MetricSpec

__all__ = ("V2HorizontalPodAutoscalerSpec",)


class V2HorizontalPodAutoscalerSpec(BaseModel):
    behavior: V2HorizontalPodAutoscalerBehavior | None = Field(None, alias="behavior")

    max_replicas: int | None = Field(None, alias="maxReplicas")

    metrics: list[V2MetricSpec] | None = Field(None, alias="metrics")

    min_replicas: int | None = Field(None, alias="minReplicas")

    scale_target_ref: V2CrossVersionObjectReference | None = Field(
        None, alias="scaleTargetRef"
    )
