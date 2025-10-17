from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V2MetricTarget",)


class V2MetricTarget(BaseModel):
    average_utilization: int | None = Field(
        default_factory=lambda: None, alias="averageUtilization"
    )

    average_value: str | None = Field(
        default_factory=lambda: None, alias="averageValue"
    )

    type: str | None = Field(default_factory=lambda: None)

    value: str | None = Field(default_factory=lambda: None)
