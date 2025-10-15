from pydantic import BaseModel, Field

from .v2_cross_version_object_reference import V2CrossVersionObjectReference
from .v2_metric_identifier import V2MetricIdentifier
from .v2_metric_target import V2MetricTarget


class V2ObjectMetricSource(BaseModel):
    described_object: V2CrossVersionObjectReference | None = Field(
        None, alias="describedObject"
    )

    metric: V2MetricIdentifier | None = Field(None, alias="metric")

    target: V2MetricTarget | None = Field(None, alias="target")
