from pydantic import BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1beta2_device_claim import V1beta2DeviceClaim
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta2ResourceClaimSpec",)


class V1beta2ResourceClaimSpec(BaseModel):
    devices: Annotated[
        V1beta2DeviceClaim, BeforeValidator(_default_if_none(V1beta2DeviceClaim))
    ] = Field(default_factory=lambda: V1beta2DeviceClaim(), exclude_if=_exclude_if)
