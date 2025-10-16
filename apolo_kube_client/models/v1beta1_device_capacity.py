from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1beta1DeviceCapacity",)


class V1beta1DeviceCapacity(BaseModel):
    value: str | None = Field(None, alias="value")
