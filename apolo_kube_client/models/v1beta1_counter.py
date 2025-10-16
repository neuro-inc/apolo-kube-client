from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1beta1Counter",)


class V1beta1Counter(BaseModel):
    value: str | None = Field(default_factory=lambda: None, alias="value")
