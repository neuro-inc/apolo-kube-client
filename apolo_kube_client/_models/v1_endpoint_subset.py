from pydantic import AliasChoices, BaseModel, Field
from .core_v1_endpoint_port import CoreV1EndpointPort
from .v1_endpoint_address import V1EndpointAddress

__all__ = ("V1EndpointSubset",)


class V1EndpointSubset(BaseModel):
    addresses: list[V1EndpointAddress] = []

    not_ready_addresses: list[V1EndpointAddress] = Field(
        default=[],
        serialization_alias="notReadyAddresses",
        validation_alias=AliasChoices("not_ready_addresses", "notReadyAddresses"),
    )

    ports: list[CoreV1EndpointPort] = []
