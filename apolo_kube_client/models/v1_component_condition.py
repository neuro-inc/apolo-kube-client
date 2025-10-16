from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ComponentCondition",)


class V1ComponentCondition(BaseModel):
    error: str | None = Field(default_factory=lambda: None, alias="error")

    message: str | None = Field(default_factory=lambda: None, alias="message")

    status: str | None = Field(default_factory=lambda: None, alias="status")

    type: str | None = Field(default_factory=lambda: None, alias="type")
