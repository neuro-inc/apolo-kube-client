from pydantic import BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v2_metric_identifier import V2MetricIdentifier
from .v2_metric_target import V2MetricTarget
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V2ExternalMetricSource",)


class V2ExternalMetricSource(BaseModel):
    metric: Annotated[
        V2MetricIdentifier, BeforeValidator(_default_if_none(V2MetricIdentifier))
    ] = Field(default_factory=lambda: V2MetricIdentifier(), exclude_if=_exclude_if)

    target: Annotated[
        V2MetricTarget, BeforeValidator(_default_if_none(V2MetricTarget))
    ] = Field(default_factory=lambda: V2MetricTarget(), exclude_if=_exclude_if)
