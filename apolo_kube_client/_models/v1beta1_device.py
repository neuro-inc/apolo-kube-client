from pydantic import BaseModel, Field
from .base import _default_if_none
from .v1beta1_basic_device import V1beta1BasicDevice
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1Device",)


class V1beta1Device(BaseModel):
    basic: Annotated[
        V1beta1BasicDevice, BeforeValidator(_default_if_none(V1beta1BasicDevice))
    ] = Field(default_factory=lambda: V1beta1BasicDevice())

    name: str | None = None
