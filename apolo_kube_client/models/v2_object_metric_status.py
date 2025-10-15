from pydantic import BaseModel, Field

from .v2_cross_version_object_reference import V2CrossVersionObjectReference
from .v2_metric_identifier import V2MetricIdentifier
from .v2_metric_value_status import V2MetricValueStatus


class V2ObjectMetricStatus(BaseModel):
    current: V2MetricValueStatus | None = Field(None, alias="current")

    described_object: V2CrossVersionObjectReference | None = Field(
        None, alias="describedObject"
    )

    metric: V2MetricIdentifier | None = Field(None, alias="metric")
