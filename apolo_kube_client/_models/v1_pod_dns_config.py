from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_pod_dns_config_option import V1PodDNSConfigOption
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PodDNSConfig",)


class V1PodDNSConfig(BaseModel):
    nameservers: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(default=[], exclude_if=_exclude_if)
    )

    options: Annotated[
        list[V1PodDNSConfigOption], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    searches: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[], exclude_if=_exclude_if
    )
