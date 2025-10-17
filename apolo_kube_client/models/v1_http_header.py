from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1HTTPHeader",)


class V1HTTPHeader(BaseModel):
    name: str | None = Field(default=None)

    value: str | None = Field(default=None)
