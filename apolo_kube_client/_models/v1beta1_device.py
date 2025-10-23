from pydantic import BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1beta1_basic_device import V1beta1BasicDevice
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1Device",)


class V1beta1Device(BaseModel):
    basic: Annotated[
        V1beta1BasicDevice, BeforeValidator(_default_if_none(V1beta1BasicDevice))
    ] = Field(default_factory=lambda: V1beta1BasicDevice(), exclude_if=_exclude_if)

    name: str | None = Field(default=None, exclude_if=_exclude_if)
