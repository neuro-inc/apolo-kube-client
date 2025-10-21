from pydantic import BaseModel, Field
from .base import _default_if_none
from .v2_metric_identifier import V2MetricIdentifier
from .v2_metric_value_status import V2MetricValueStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V2PodsMetricStatus",)


class V2PodsMetricStatus(BaseModel):
    current: Annotated[
        V2MetricValueStatus, BeforeValidator(_default_if_none(V2MetricValueStatus))
    ] = Field(default_factory=lambda: V2MetricValueStatus())

    metric: Annotated[
        V2MetricIdentifier, BeforeValidator(_default_if_none(V2MetricIdentifier))
    ] = Field(default_factory=lambda: V2MetricIdentifier())
