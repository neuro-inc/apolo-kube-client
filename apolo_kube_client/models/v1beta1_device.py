from __future__ import annotations

from pydantic import BaseModel, Field

from .v1beta1_basic_device import V1beta1BasicDevice

__all__ = ("V1beta1Device",)


class V1beta1Device(BaseModel):
    basic: V1beta1BasicDevice | None = Field(None, alias="basic")

    name: str | None = Field(None, alias="name")
