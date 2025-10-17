from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1beta2DeviceToleration",)


class V1beta2DeviceToleration(BaseModel):
    effect: str | None = Field(default_factory=lambda: None)

    key: str | None = Field(default_factory=lambda: None)

    operator: str | None = Field(default_factory=lambda: None)

    toleration_seconds: int | None = Field(
        default_factory=lambda: None, alias="tolerationSeconds"
    )

    value: str | None = Field(default_factory=lambda: None)
