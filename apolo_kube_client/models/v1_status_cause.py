from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1StatusCause",)


class V1StatusCause(BaseModel):
    field: str | None = Field(default_factory=lambda: None, alias="field")

    message: str | None = Field(default_factory=lambda: None, alias="message")

    reason: str | None = Field(default_factory=lambda: None, alias="reason")
