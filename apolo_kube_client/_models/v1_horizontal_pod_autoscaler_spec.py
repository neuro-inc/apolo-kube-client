from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_cross_version_object_reference import V1CrossVersionObjectReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1HorizontalPodAutoscalerSpec",)


class V1HorizontalPodAutoscalerSpec(BaseModel):
    max_replicas: int | None = Field(
        default=None,
        serialization_alias="maxReplicas",
        validation_alias=AliasChoices("max_replicas", "maxReplicas"),
        exclude_if=_exclude_if,
    )

    min_replicas: int | None = Field(
        default=None,
        serialization_alias="minReplicas",
        validation_alias=AliasChoices("min_replicas", "minReplicas"),
        exclude_if=_exclude_if,
    )

    scale_target_ref: Annotated[
        V1CrossVersionObjectReference,
        BeforeValidator(_default_if_none(V1CrossVersionObjectReference)),
    ] = Field(
        default_factory=lambda: V1CrossVersionObjectReference(),
        serialization_alias="scaleTargetRef",
        validation_alias=AliasChoices("scale_target_ref", "scaleTargetRef"),
        exclude_if=_exclude_if,
    )

    target_cpu_utilization_percentage: int | None = Field(
        default=None,
        serialization_alias="targetCPUUtilizationPercentage",
        validation_alias=AliasChoices(
            "target_cpu_utilization_percentage", "targetCPUUtilizationPercentage"
        ),
        exclude_if=_exclude_if,
    )
