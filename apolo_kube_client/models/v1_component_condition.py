from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ComponentCondition",)


class V1ComponentCondition(BaseModel):
    error: str | None = Field(default_factory=lambda: None)

    message: str | None = Field(default_factory=lambda: None)

    status: str | None = Field(default_factory=lambda: None)

    type: str | None = Field(default_factory=lambda: None)
