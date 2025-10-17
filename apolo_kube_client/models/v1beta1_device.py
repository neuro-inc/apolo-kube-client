from pydantic import BaseModel, Field
from .v1beta1_basic_device import V1beta1BasicDevice

__all__ = ("V1beta1Device",)


class V1beta1Device(BaseModel):
    basic: V1beta1BasicDevice = Field(default_factory=lambda: V1beta1BasicDevice())

    name: str | None = None
