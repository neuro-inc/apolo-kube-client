from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1beta2CELDeviceSelector",)


class V1beta2CELDeviceSelector(BaseModel):
    expression: str | None = Field(default_factory=lambda: None, alias="expression")
