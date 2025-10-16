from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1CELDeviceSelector",)


class V1CELDeviceSelector(BaseModel):
    expression: str | None = Field(default_factory=lambda: None, alias="expression")
