from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V2MetricValueStatus",)


class V2MetricValueStatus(BaseModel):
    average_utilization: int | None = Field(None, alias="averageUtilization")

    average_value: str | None = Field(None, alias="averageValue")

    value: str | None = Field(None, alias="value")
