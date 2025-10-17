from __future__ import annotations
from pydantic import BaseModel, Field
from .v2_metric_identifier import V2MetricIdentifier
from .v2_metric_value_status import V2MetricValueStatus

__all__ = ("V2PodsMetricStatus",)


class V2PodsMetricStatus(BaseModel):
    current: V2MetricValueStatus = Field(default_factory=lambda: V2MetricValueStatus())

    metric: V2MetricIdentifier = Field(default_factory=lambda: V2MetricIdentifier())
