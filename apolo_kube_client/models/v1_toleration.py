from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1Toleration",)


class V1Toleration(BaseModel):
    effect: str | None = Field(None, alias="effect")

    key: str | None = Field(None, alias="key")

    operator: str | None = Field(None, alias="operator")

    toleration_seconds: int | None = Field(None, alias="tolerationSeconds")

    value: str | None = Field(None, alias="value")
