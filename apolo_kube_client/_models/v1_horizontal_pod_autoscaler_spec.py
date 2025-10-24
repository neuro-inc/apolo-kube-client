from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_cross_version_object_reference import V1CrossVersionObjectReference

__all__ = ("V1HorizontalPodAutoscalerSpec",)


class V1HorizontalPodAutoscalerSpec(BaseModel):
    """specification of a horizontal pod autoscaler."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.autoscaling.v1.HorizontalPodAutoscalerSpec"
    )

    max_replicas: Annotated[
        int,
        Field(
            alias="maxReplicas",
            description="""maxReplicas is the upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas.""",
        ),
    ]

    min_replicas: Annotated[
        int | None,
        Field(
            alias="minReplicas",
            description="""minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is active as long as at least one metric value is available.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    scale_target_ref: Annotated[
        V1CrossVersionObjectReference,
        Field(
            alias="scaleTargetRef",
            description="""reference to scaled resource; horizontal pod autoscaler will learn the current resource consumption and will set the desired number of pods by using its Scale subresource.""",
        ),
    ]

    target_cpu_utilization_percentage: Annotated[
        int | None,
        Field(
            alias="targetCPUUtilizationPercentage",
            description="""targetCPUUtilizationPercentage is the target average CPU utilization (represented as a percentage of requested CPU) over all the pods; if not specified the default autoscaling policy will be used.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
