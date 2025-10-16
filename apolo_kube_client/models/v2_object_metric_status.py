from __future__ import annotations
from pydantic import BaseModel, Field
from .v2_cross_version_object_reference import V2CrossVersionObjectReference
from .v2_metric_identifier import V2MetricIdentifier
from .v2_metric_value_status import V2MetricValueStatus

__all__ = ("V2ObjectMetricStatus",)


class V2ObjectMetricStatus(BaseModel):
    current: V2MetricValueStatus = Field(
        default_factory=lambda: V2MetricValueStatus(), alias="current"
    )

    described_object: V2CrossVersionObjectReference = Field(
        default_factory=lambda: V2CrossVersionObjectReference(), alias="describedObject"
    )

    metric: V2MetricIdentifier = Field(
        default_factory=lambda: V2MetricIdentifier(), alias="metric"
    )
