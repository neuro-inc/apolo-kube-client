from pydantic import AliasChoices, Field
from .base import ResourceModel
from .discovery_v1_endpoint_port import DiscoveryV1EndpointPort
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_endpoint import V1Endpoint
from .v1_object_meta import V1ObjectMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1EndpointSlice",)


class V1EndpointSlice(ResourceModel):
    address_type: str | None = Field(
        default=None,
        serialization_alias="addressType",
        validation_alias=AliasChoices("address_type", "addressType"),
        exclude_if=_exclude_if,
    )

    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
        exclude_if=_exclude_if,
    )

    endpoints: Annotated[
        list[V1Endpoint], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta(), exclude_if=_exclude_if)

    ports: Annotated[
        list[DiscoveryV1EndpointPort], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)
