from pydantic import BaseModel, Field
from .utils import _default_if_none
from .v1_device_claim import V1DeviceClaim
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ResourceClaimSpec",)


class V1ResourceClaimSpec(BaseModel):
    devices: Annotated[
        V1DeviceClaim, BeforeValidator(_default_if_none(V1DeviceClaim))
    ] = Field(default_factory=lambda: V1DeviceClaim())
