from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta1_basic_device import V1beta1BasicDevice

__all__ = ("V1beta1Device",)


class V1beta1Device(BaseModel):
    basic: V1beta1BasicDevice = Field(
        default_factory=lambda: V1beta1BasicDevice(), alias="basic"
    )

    name: str | None = Field(default_factory=lambda: None, alias="name")
