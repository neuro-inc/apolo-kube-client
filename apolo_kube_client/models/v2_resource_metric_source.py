from __future__ import annotations

from pydantic import BaseModel, Field

from .v2_metric_target import V2MetricTarget

__all__ = ("V2ResourceMetricSource",)


class V2ResourceMetricSource(BaseModel):
    name: str | None = Field(None, alias="name")

    target: V2MetricTarget | None = Field(None, alias="target")
