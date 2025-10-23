from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_opaque_device_configuration import V1OpaqueDeviceConfiguration
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1DeviceAllocationConfiguration",)


class V1DeviceAllocationConfiguration(BaseModel):
    opaque: Annotated[
        V1OpaqueDeviceConfiguration,
        BeforeValidator(_default_if_none(V1OpaqueDeviceConfiguration)),
    ] = Field(
        default_factory=lambda: V1OpaqueDeviceConfiguration(), exclude_if=_exclude_if
    )

    requests: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[], exclude_if=_exclude_if
    )

    source: str | None = Field(default=None, exclude_if=_exclude_if)
