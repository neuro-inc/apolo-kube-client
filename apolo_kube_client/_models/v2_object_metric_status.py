from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .v2_cross_version_object_reference import V2CrossVersionObjectReference
from .v2_metric_identifier import V2MetricIdentifier
from .v2_metric_value_status import V2MetricValueStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V2ObjectMetricStatus",)


class V2ObjectMetricStatus(BaseModel):
    current: Annotated[
        V2MetricValueStatus, BeforeValidator(_default_if_none(V2MetricValueStatus))
    ] = Field(default_factory=lambda: V2MetricValueStatus())

    described_object: Annotated[
        V2CrossVersionObjectReference,
        BeforeValidator(_default_if_none(V2CrossVersionObjectReference)),
    ] = Field(
        default_factory=lambda: V2CrossVersionObjectReference(),
        serialization_alias="describedObject",
        validation_alias=AliasChoices("described_object", "describedObject"),
    )

    metric: Annotated[
        V2MetricIdentifier, BeforeValidator(_default_if_none(V2MetricIdentifier))
    ] = Field(default_factory=lambda: V2MetricIdentifier())
