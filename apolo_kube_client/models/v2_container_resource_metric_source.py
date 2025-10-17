from __future__ import annotations
from pydantic import BaseModel, Field
from .v2_metric_target import V2MetricTarget

__all__ = ("V2ContainerResourceMetricSource",)


class V2ContainerResourceMetricSource(BaseModel):
    container: str | None = Field(default=None)

    name: str | None = Field(default=None)

    target: V2MetricTarget = Field(default_factory=lambda: V2MetricTarget())
