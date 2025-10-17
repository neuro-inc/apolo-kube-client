from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1Counter",)


class V1Counter(BaseModel):
    value: str | None = Field(default=None)
