from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v2_cross_version_object_reference import V2CrossVersionObjectReference
from .v2_horizontal_pod_autoscaler_behavior import V2HorizontalPodAutoscalerBehavior
from .v2_metric_spec import V2MetricSpec
from pydantic import BeforeValidator

__all__ = ("V2HorizontalPodAutoscalerSpec",)


class V2HorizontalPodAutoscalerSpec(BaseModel):
    """HorizontalPodAutoscalerSpec describes the desired functionality of the HorizontalPodAutoscaler."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.autoscaling.v2.HorizontalPodAutoscalerSpec"
    )

    behavior: Annotated[
        V2HorizontalPodAutoscalerBehavior,
        Field(
            description="""behavior configures the scaling behavior of the target in both Up and Down directions (scaleUp and scaleDown fields respectively). If not set, the default HPAScalingRules for scale up and scale down are used.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V2HorizontalPodAutoscalerBehavior)),
    ] = V2HorizontalPodAutoscalerBehavior()

    max_replicas: Annotated[
        int,
        Field(
            alias="maxReplicas",
            description="""maxReplicas is the upper limit for the number of replicas to which the autoscaler can scale up. It cannot be less that minReplicas.""",
        ),
    ]

    metrics: Annotated[
        list[V2MetricSpec],
        Field(
            description="""metrics contains the specifications for which to use to calculate the desired replica count (the maximum replica count across all metrics will be used).  The desired replica count is calculated multiplying the ratio between the target value and the current value by the current number of pods.  Ergo, metrics used must decrease as the pod count is increased, and vice-versa.  See the individual metric source types for more information about how each type of metric must respond. If not set, the default metric will be set to 80% average CPU utilization.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    min_replicas: Annotated[
        int | None,
        Field(
            alias="minReplicas",
            description="""minReplicas is the lower limit for the number of replicas to which the autoscaler can scale down.  It defaults to 1 pod.  minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured.  Scaling is active as long as at least one metric value is available.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    scale_target_ref: Annotated[
        V2CrossVersionObjectReference,
        Field(
            alias="scaleTargetRef",
            description="""scaleTargetRef points to the target resource to scale, and is used to the pods for which metrics should be collected, as well as to actually change the replica count.""",
        ),
    ]
