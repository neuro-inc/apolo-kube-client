from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V2HPAScalingPolicy",)


class V2HPAScalingPolicy(BaseModel):
    period_seconds: int | None = Field(
        default_factory=lambda: None, alias="periodSeconds"
    )

    type: str | None = Field(default_factory=lambda: None, alias="type")

    value: int | None = Field(default_factory=lambda: None, alias="value")
