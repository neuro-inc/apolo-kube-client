from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_port_status import V1PortStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1LoadBalancerIngress",)


class V1LoadBalancerIngress(BaseModel):
    hostname: str | None = Field(default=None, exclude_if=_exclude_if)

    ip: str | None = Field(default=None, exclude_if=_exclude_if)

    ip_mode: str | None = Field(
        default=None,
        serialization_alias="ipMode",
        validation_alias=AliasChoices("ip_mode", "ipMode"),
        exclude_if=_exclude_if,
    )

    ports: Annotated[list[V1PortStatus], BeforeValidator(_collection_if_none("[]"))] = (
        Field(default=[], exclude_if=_exclude_if)
    )
