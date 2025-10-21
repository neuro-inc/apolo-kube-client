from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v2_horizontal_pod_autoscaler_condition import V2HorizontalPodAutoscalerCondition
from .v2_metric_status import V2MetricStatus
from datetime import datetime
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V2HorizontalPodAutoscalerStatus",)


class V2HorizontalPodAutoscalerStatus(BaseModel):
    conditions: Annotated[
        list[V2HorizontalPodAutoscalerCondition],
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    current_metrics: Annotated[
        list[V2MetricStatus], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
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
