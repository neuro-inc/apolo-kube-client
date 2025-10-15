from pydantic import BaseModel, Field

from .v2_metric_target import V2MetricTarget


class V2ResourceMetricSource(BaseModel):
    name: str | None = Field(None, alias="name")

    target: V2MetricTarget | None = Field(None, alias="target")
