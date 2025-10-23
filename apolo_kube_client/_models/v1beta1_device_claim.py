from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1beta1_device_claim_configuration import V1beta1DeviceClaimConfiguration
from .v1beta1_device_constraint import V1beta1DeviceConstraint
from .v1beta1_device_request import V1beta1DeviceRequest
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1DeviceClaim",)


class V1beta1DeviceClaim(BaseModel):
    config: Annotated[
        list[V1beta1DeviceClaimConfiguration],
        BeforeValidator(_collection_if_none("[]")),
    ] = Field(default=[], exclude_if=_exclude_if)

    constraints: Annotated[
        list[V1beta1DeviceConstraint], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    requests: Annotated[
        list[V1beta1DeviceRequest], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)
