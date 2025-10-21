from pydantic import BaseModel, Field
from .utils import _default_if_none
from .v2_metric_identifier import V2MetricIdentifier
from .v2_metric_target import V2MetricTarget
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V2PodsMetricSource",)


class V2PodsMetricSource(BaseModel):
    metric: Annotated[
        V2MetricIdentifier, BeforeValidator(_default_if_none(V2MetricIdentifier))
    ] = Field(default_factory=lambda: V2MetricIdentifier())

    target: Annotated[
        V2MetricTarget, BeforeValidator(_default_if_none(V2MetricTarget))
    ] = Field(default_factory=lambda: V2MetricTarget())
