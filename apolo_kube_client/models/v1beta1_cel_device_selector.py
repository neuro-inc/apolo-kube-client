from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1beta1CELDeviceSelector",)


class V1beta1CELDeviceSelector(BaseModel):
    expression: str | None = Field(default=None)
