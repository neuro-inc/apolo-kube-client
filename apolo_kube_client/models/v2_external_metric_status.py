from __future__ import annotations

from pydantic import BaseModel, Field

from .v2_metric_identifier import V2MetricIdentifier
from .v2_metric_value_status import V2MetricValueStatus

__all__ = ("V2ExternalMetricStatus",)


class V2ExternalMetricStatus(BaseModel):
    current: V2MetricValueStatus | None = Field(None, alias="current")

    metric: V2MetricIdentifier | None = Field(None, alias="metric")
