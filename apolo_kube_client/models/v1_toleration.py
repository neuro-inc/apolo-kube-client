from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1Toleration",)


class V1Toleration(BaseModel):
    effect: str | None = Field(default_factory=lambda: None, alias="effect")

    key: str | None = Field(default_factory=lambda: None, alias="key")

    operator: str | None = Field(default_factory=lambda: None, alias="operator")

    toleration_seconds: int | None = Field(
        default_factory=lambda: None, alias="tolerationSeconds"
    )

    value: str | None = Field(default_factory=lambda: None, alias="value")
