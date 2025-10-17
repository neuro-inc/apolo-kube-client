from pydantic import BaseModel, Field
from .v2_metric_identifier import V2MetricIdentifier
from .v2_metric_target import V2MetricTarget

__all__ = ("V2ExternalMetricSource",)


class V2ExternalMetricSource(BaseModel):
    metric: V2MetricIdentifier = Field(default_factory=lambda: V2MetricIdentifier())

    target: V2MetricTarget = Field(default_factory=lambda: V2MetricTarget())
