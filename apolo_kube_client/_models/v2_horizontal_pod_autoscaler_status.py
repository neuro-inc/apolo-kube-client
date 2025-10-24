from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v2_horizontal_pod_autoscaler_condition import V2HorizontalPodAutoscalerCondition
from .v2_metric_status import V2MetricStatus
from datetime import datetime
from pydantic import BeforeValidator

__all__ = ("V2HorizontalPodAutoscalerStatus",)


class V2HorizontalPodAutoscalerStatus(BaseModel):
    """HorizontalPodAutoscalerStatus describes the current status of a horizontal pod autoscaler."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.autoscaling.v2.HorizontalPodAutoscalerStatus"
    )

    conditions: Annotated[
        list[V2HorizontalPodAutoscalerCondition],
        Field(
            description="""conditions is the set of conditions required for this autoscaler to scale its target, and indicates whether or not those conditions are met.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    current_metrics: Annotated[
        list[V2MetricStatus],
        Field(
            alias="currentMetrics",
            description="""currentMetrics is the last read state of the metrics used by this autoscaler.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    current_replicas: Annotated[
        int | None,
        Field(
            alias="currentReplicas",
            description="""currentReplicas is current number of replicas of pods managed by this autoscaler, as last seen by the autoscaler.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    desired_replicas: Annotated[
        int,
        Field(
            alias="desiredReplicas",
            description="""desiredReplicas is the desired number of replicas of pods managed by this autoscaler, as last calculated by the autoscaler.""",
        ),
    ]

    last_scale_time: Annotated[
        datetime | None,
        Field(
            alias="lastScaleTime",
            description="""lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods, used by the autoscaler to control how often the number of pods is changed.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    observed_generation: Annotated[
        int | None,
        Field(
            alias="observedGeneration",
            description="""observedGeneration is the most recent generation observed by this autoscaler.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
