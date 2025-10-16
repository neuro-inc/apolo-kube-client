from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1StatusCause",)


class V1StatusCause(BaseModel):
    field: str | None = Field(None, alias="field")

    message: str | None = Field(None, alias="message")

    reason: str | None = Field(None, alias="reason")
