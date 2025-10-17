from __future__ import annotations
from pydantic import BaseModel, Field
from .v2_metric_identifier import V2MetricIdentifier
from .v2_metric_target import V2MetricTarget

__all__ = ("V2PodsMetricSource",)


class V2PodsMetricSource(BaseModel):
    metric: V2MetricIdentifier = Field(default_factory=lambda: V2MetricIdentifier())

    target: V2MetricTarget = Field(default_factory=lambda: V2MetricTarget())
