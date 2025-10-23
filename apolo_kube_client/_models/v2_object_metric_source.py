from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v2_cross_version_object_reference import V2CrossVersionObjectReference
from .v2_metric_identifier import V2MetricIdentifier
from .v2_metric_target import V2MetricTarget
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V2ObjectMetricSource",)


class V2ObjectMetricSource(BaseModel):
    described_object: Annotated[
        V2CrossVersionObjectReference,
        BeforeValidator(_default_if_none(V2CrossVersionObjectReference)),
    ] = Field(
        default_factory=lambda: V2CrossVersionObjectReference(),
        serialization_alias="describedObject",
        validation_alias=AliasChoices("described_object", "describedObject"),
        exclude_if=_exclude_if,
    )

    metric: Annotated[
        V2MetricIdentifier, BeforeValidator(_default_if_none(V2MetricIdentifier))
    ] = Field(default_factory=lambda: V2MetricIdentifier(), exclude_if=_exclude_if)

    target: Annotated[
        V2MetricTarget, BeforeValidator(_default_if_none(V2MetricTarget))
    ] = Field(default_factory=lambda: V2MetricTarget(), exclude_if=_exclude_if)
