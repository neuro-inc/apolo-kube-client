from __future__ import annotations
from pydantic import BaseModel, Field
from .v2_metric_value_status import V2MetricValueStatus

__all__ = ("V2ContainerResourceMetricStatus",)


class V2ContainerResourceMetricStatus(BaseModel):
    container: str | None = Field(default=None)

    current: V2MetricValueStatus = Field(default_factory=lambda: V2MetricValueStatus())

    name: str | None = Field(default=None)
