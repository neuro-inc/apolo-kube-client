from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1StatusCause",)


class V1StatusCause(BaseModel):
    field: str | None = Field(default_factory=lambda: None)

    message: str | None = Field(default_factory=lambda: None)

    reason: str | None = Field(default_factory=lambda: None)
