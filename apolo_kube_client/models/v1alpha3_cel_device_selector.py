from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1alpha3CELDeviceSelector",)


class V1alpha3CELDeviceSelector(BaseModel):
    expression: str | None = Field(default=None)
