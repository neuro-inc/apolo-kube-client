from pydantic import AliasChoices, BaseModel, Field
from .core_v1_endpoint_port import CoreV1EndpointPort
from .utils import _collection_if_none
from .v1_endpoint_address import V1EndpointAddress
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1EndpointSubset",)


class V1EndpointSubset(BaseModel):
    addresses: Annotated[
        list[V1EndpointAddress], BeforeValidator(_collection_if_none("[]"))
    ] = []

    not_ready_addresses: Annotated[
        list[V1EndpointAddress], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="notReadyAddresses",
        validation_alias=AliasChoices("not_ready_addresses", "notReadyAddresses"),
    )

    ports: Annotated[
        list[CoreV1EndpointPort], BeforeValidator(_collection_if_none("[]"))
    ] = []
