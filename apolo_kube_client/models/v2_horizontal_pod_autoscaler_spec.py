from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v2_cross_version_object_reference import V2CrossVersionObjectReference
from .v2_horizontal_pod_autoscaler_behavior import V2HorizontalPodAutoscalerBehavior
from .v2_metric_spec import V2MetricSpec

__all__ = ("V2HorizontalPodAutoscalerSpec",)


class V2HorizontalPodAutoscalerSpec(BaseModel):
    behavior: V2HorizontalPodAutoscalerBehavior = Field(
        default_factory=lambda: V2HorizontalPodAutoscalerBehavior()
    )

    max_replicas: int | None = Field(
        default=None,
        serialization_alias="maxReplicas",
        validation_alias=AliasChoices("max_replicas", "maxReplicas"),
    )

    metrics: list[V2MetricSpec] = Field(default=[])

    min_replicas: int | None = Field(
        default=None,
        serialization_alias="minReplicas",
        validation_alias=AliasChoices("min_replicas", "minReplicas"),
    )

    scale_target_ref: V2CrossVersionObjectReference = Field(
        default_factory=lambda: V2CrossVersionObjectReference(),
        serialization_alias="scaleTargetRef",
        validation_alias=AliasChoices("scale_target_ref", "scaleTargetRef"),
    )
