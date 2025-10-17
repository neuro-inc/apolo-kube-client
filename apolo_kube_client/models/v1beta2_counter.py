from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1beta2Counter",)


class V1beta2Counter(BaseModel):
    value: str | None = Field(default=None)
