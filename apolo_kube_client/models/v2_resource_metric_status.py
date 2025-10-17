from pydantic import BaseModel, Field
from .v2_metric_value_status import V2MetricValueStatus

__all__ = ("V2ResourceMetricStatus",)


class V2ResourceMetricStatus(BaseModel):
    current: V2MetricValueStatus = Field(default_factory=lambda: V2MetricValueStatus())

    name: str | None = None
