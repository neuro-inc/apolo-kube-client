from pydantic import BaseModel, Field
from .utils import _default_if_none
from .v1beta1_device_claim import V1beta1DeviceClaim
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1ResourceClaimSpec",)


class V1beta1ResourceClaimSpec(BaseModel):
    devices: Annotated[
        V1beta1DeviceClaim, BeforeValidator(_default_if_none(V1beta1DeviceClaim))
    ] = Field(default_factory=lambda: V1beta1DeviceClaim())
