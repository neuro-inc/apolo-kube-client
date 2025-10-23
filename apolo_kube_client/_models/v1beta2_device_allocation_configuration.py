from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1beta2_opaque_device_configuration import V1beta2OpaqueDeviceConfiguration
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta2DeviceAllocationConfiguration",)


class V1beta2DeviceAllocationConfiguration(BaseModel):
    opaque: Annotated[
        V1beta2OpaqueDeviceConfiguration,
        BeforeValidator(_default_if_none(V1beta2OpaqueDeviceConfiguration)),
    ] = Field(
        default_factory=lambda: V1beta2OpaqueDeviceConfiguration(),
        exclude_if=_exclude_if,
    )

    requests: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[], exclude_if=_exclude_if
    )

    source: str | None = Field(default=None, exclude_if=_exclude_if)
