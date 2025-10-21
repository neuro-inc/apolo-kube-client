from pydantic import BaseModel
from .utils import _collection_if_none
from .v1_pod_dns_config_option import V1PodDNSConfigOption
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PodDNSConfig",)


class V1PodDNSConfig(BaseModel):
    nameservers: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []

    options: Annotated[
        list[V1PodDNSConfigOption], BeforeValidator(_collection_if_none("[]"))
    ] = []

    searches: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []
