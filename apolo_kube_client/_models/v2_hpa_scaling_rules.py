from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v2_hpa_scaling_policy import V2HPAScalingPolicy
from pydantic import BeforeValidator

__all__ = ("V2HPAScalingRules",)


class V2HPAScalingRules(BaseModel):
    """HPAScalingRules configures the scaling behavior for one direction via scaling Policy Rules and a configurable metric tolerance.

    Scaling Policy Rules are applied after calculating DesiredReplicas from metrics for the HPA. They can limit the scaling velocity by specifying scaling policies. They can prevent flapping by specifying the stabilization window, so that the number of replicas is not set instantly, instead, the safest value from the stabilization window is chosen.

    The tolerance is applied to the metric values and prevents scaling too eagerly for small metric variations. (Note that setting a tolerance requires enabling the alpha HPAConfigurableTolerance feature gate.)"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.autoscaling.v2.HPAScalingRules"

    policies: Annotated[
        list[V2HPAScalingPolicy],
        Field(
            description="""policies is a list of potential scaling polices which can be used during scaling. If not set, use the default values: - For scale up: allow doubling the number of pods, or an absolute change of 4 pods in a 15s window. - For scale down: allow all pods to be removed in a 15s window.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    select_policy: Annotated[
        str | None,
        Field(
            alias="selectPolicy",
            description="""selectPolicy is used to specify which policy should be used. If not set, the default value Max is used.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    stabilization_window_seconds: Annotated[
        int | None,
        Field(
            alias="stabilizationWindowSeconds",
            description="""stabilizationWindowSeconds is the number of seconds for which past recommendations should be considered while scaling up or scaling down. StabilizationWindowSeconds must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long).""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    tolerance: Annotated[
        str | None,
        Field(
            description="""tolerance is the tolerance on the ratio between the current and desired metric value under which no updates are made to the desired number of replicas (e.g. 0.01 for 1%). Must be greater than or equal to zero. If not set, the default cluster-wide tolerance is applied (by default 10%).

For example, if autoscaling is configured with a memory consumption target of 100Mi, and scale-down and scale-up tolerances of 5% and 1% respectively, scaling will be triggered when the actual consumption falls below 95Mi or exceeds 101Mi.

This is an alpha field and requires enabling the HPAConfigurableTolerance feature gate.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
