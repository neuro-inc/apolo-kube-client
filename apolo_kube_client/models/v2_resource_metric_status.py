from __future__ import annotations

from pydantic import BaseModel, Field

from .v2_metric_value_status import V2MetricValueStatus

__all__ = ("V2ResourceMetricStatus",)


class V2ResourceMetricStatus(BaseModel):
    current: V2MetricValueStatus | None = Field(None, alias="current")

    name: str | None = Field(None, alias="name")
