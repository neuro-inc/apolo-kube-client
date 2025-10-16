from __future__ import annotations

from pydantic import BaseModel, Field

from .v2_metric_identifier import V2MetricIdentifier
from .v2_metric_target import V2MetricTarget

__all__ = ("V2ExternalMetricSource",)


class V2ExternalMetricSource(BaseModel):
    metric: V2MetricIdentifier | None = Field(None, alias="metric")

    target: V2MetricTarget | None = Field(None, alias="target")
