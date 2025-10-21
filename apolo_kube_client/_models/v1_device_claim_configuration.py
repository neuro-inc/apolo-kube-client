from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_opaque_device_configuration import V1OpaqueDeviceConfiguration
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1DeviceClaimConfiguration",)


class V1DeviceClaimConfiguration(BaseModel):
    opaque: Annotated[
        V1OpaqueDeviceConfiguration,
        BeforeValidator(_default_if_none(V1OpaqueDeviceConfiguration)),
    ] = Field(default_factory=lambda: V1OpaqueDeviceConfiguration())

    requests: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []
