from pydantic import BaseModel, Field

from .core_v1_endpoint_port import CoreV1EndpointPort
from .v1_endpoint_address import V1EndpointAddress


class V1EndpointSubset(BaseModel):
    addresses: list[V1EndpointAddress] | None = Field(None, alias="addresses")

    not_ready_addresses: list[V1EndpointAddress] | None = Field(
        None, alias="notReadyAddresses"
    )

    ports: list[CoreV1EndpointPort] | None = Field(None, alias="ports")
