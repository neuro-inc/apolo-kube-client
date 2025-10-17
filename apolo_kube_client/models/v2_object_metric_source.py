from __future__ import annotations
from pydantic import BaseModel, Field
from .v2_cross_version_object_reference import V2CrossVersionObjectReference
from .v2_metric_identifier import V2MetricIdentifier
from .v2_metric_target import V2MetricTarget

__all__ = ("V2ObjectMetricSource",)


class V2ObjectMetricSource(BaseModel):
    described_object: V2CrossVersionObjectReference = Field(
        default_factory=lambda: V2CrossVersionObjectReference(), alias="describedObject"
    )

    metric: V2MetricIdentifier = Field(default_factory=lambda: V2MetricIdentifier())

    target: V2MetricTarget = Field(default_factory=lambda: V2MetricTarget())
