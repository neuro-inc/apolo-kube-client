from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1beta2_device_claim_configuration import V1beta2DeviceClaimConfiguration
from .v1beta2_device_constraint import V1beta2DeviceConstraint
from .v1beta2_device_request import V1beta2DeviceRequest
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta2DeviceClaim",)


class V1beta2DeviceClaim(BaseModel):
    config: Annotated[
        list[V1beta2DeviceClaimConfiguration],
        BeforeValidator(_collection_if_none("[]")),
    ] = Field(default=[], exclude_if=_exclude_if)

    constraints: Annotated[
        list[V1beta2DeviceConstraint], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    requests: Annotated[
        list[V1beta2DeviceRequest], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)
