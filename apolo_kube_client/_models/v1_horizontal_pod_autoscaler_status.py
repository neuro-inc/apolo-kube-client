from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

__all__ = ("V1HorizontalPodAutoscalerStatus",)


class V1HorizontalPodAutoscalerStatus(BaseModel):
    """current status of a horizontal pod autoscaler"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.autoscaling.v1.HorizontalPodAutoscalerStatus"
    )

    current_cpu_utilization_percentage: Annotated[
        int | None,
        Field(
            alias="currentCPUUtilizationPercentage",
            description="""currentCPUUtilizationPercentage is the current average CPU utilization over all pods, represented as a percentage of requested CPU, e.g. 70 means that an average pod is using now 70% of its requested CPU.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    current_replicas: Annotated[
        int,
        Field(
            alias="currentReplicas",
            description="""currentReplicas is the current number of replicas of pods managed by this autoscaler.""",
        ),
    ]

    desired_replicas: Annotated[
        int,
        Field(
            alias="desiredReplicas",
            description="""desiredReplicas is the  desired number of replicas of pods managed by this autoscaler.""",
        ),
    ]

    last_scale_time: Annotated[
        datetime | None,
        Field(
            alias="lastScaleTime",
            description="""lastScaleTime is the last time the HorizontalPodAutoscaler scaled the number of pods; used by the autoscaler to control how often the number of pods is changed.""",
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
