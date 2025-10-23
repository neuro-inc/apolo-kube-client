from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v2_cross_version_object_reference import V2CrossVersionObjectReference
from .v2_horizontal_pod_autoscaler_behavior import V2HorizontalPodAutoscalerBehavior
from .v2_metric_spec import V2MetricSpec
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V2HorizontalPodAutoscalerSpec",)


class V2HorizontalPodAutoscalerSpec(BaseModel):
    behavior: Annotated[
        V2HorizontalPodAutoscalerBehavior,
        BeforeValidator(_default_if_none(V2HorizontalPodAutoscalerBehavior)),
    ] = Field(
        default_factory=lambda: V2HorizontalPodAutoscalerBehavior(),
        exclude_if=_exclude_if,
    )

    max_replicas: int | None = Field(
        default=None,
        serialization_alias="maxReplicas",
        validation_alias=AliasChoices("max_replicas", "maxReplicas"),
        exclude_if=_exclude_if,
    )

    metrics: Annotated[
        list[V2MetricSpec], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    min_replicas: int | None = Field(
        default=None,
        serialization_alias="minReplicas",
        validation_alias=AliasChoices("min_replicas", "minReplicas"),
        exclude_if=_exclude_if,
    )

    scale_target_ref: Annotated[
        V2CrossVersionObjectReference,
        BeforeValidator(_default_if_none(V2CrossVersionObjectReference)),
    ] = Field(
        default_factory=lambda: V2CrossVersionObjectReference(),
        serialization_alias="scaleTargetRef",
        validation_alias=AliasChoices("scale_target_ref", "scaleTargetRef"),
        exclude_if=_exclude_if,
    )
