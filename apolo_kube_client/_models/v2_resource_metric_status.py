from pydantic import BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v2_metric_value_status import V2MetricValueStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V2ResourceMetricStatus",)


class V2ResourceMetricStatus(BaseModel):
    current: Annotated[
        V2MetricValueStatus, BeforeValidator(_default_if_none(V2MetricValueStatus))
    ] = Field(default_factory=lambda: V2MetricValueStatus(), exclude_if=_exclude_if)

    name: str | None = Field(default=None, exclude_if=_exclude_if)
