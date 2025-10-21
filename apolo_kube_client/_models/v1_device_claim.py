from pydantic import BaseModel
from .utils import _collection_if_none
from .v1_device_claim_configuration import V1DeviceClaimConfiguration
from .v1_device_constraint import V1DeviceConstraint
from .v1_device_request import V1DeviceRequest
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1DeviceClaim",)


class V1DeviceClaim(BaseModel):
    config: Annotated[
        list[V1DeviceClaimConfiguration], BeforeValidator(_collection_if_none("[]"))
    ] = []

    constraints: Annotated[
        list[V1DeviceConstraint], BeforeValidator(_collection_if_none("[]"))
    ] = []

    requests: Annotated[
        list[V1DeviceRequest], BeforeValidator(_collection_if_none("[]"))
    ] = []
