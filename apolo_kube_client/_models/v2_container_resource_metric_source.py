from pydantic import BaseModel, Field
from .utils import _default_if_none
from .v2_metric_target import V2MetricTarget
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V2ContainerResourceMetricSource",)


class V2ContainerResourceMetricSource(BaseModel):
    container: str | None = None

    name: str | None = None

    target: Annotated[
        V2MetricTarget, BeforeValidator(_default_if_none(V2MetricTarget))
    ] = Field(default_factory=lambda: V2MetricTarget())
