from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1_port_status import V1PortStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1LoadBalancerIngress",)


class V1LoadBalancerIngress(BaseModel):
    hostname: str | None = None

    ip: str | None = None

    ip_mode: str | None = Field(
        default=None,
        serialization_alias="ipMode",
        validation_alias=AliasChoices("ip_mode", "ipMode"),
    )

    ports: Annotated[
        list[V1PortStatus], BeforeValidator(_collection_if_none("[]"))
    ] = []
