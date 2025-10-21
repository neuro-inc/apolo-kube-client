from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1_for_node import V1ForNode
from .v1_for_zone import V1ForZone
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1EndpointHints",)


class V1EndpointHints(BaseModel):
    for_nodes: Annotated[
        list[V1ForNode], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="forNodes",
        validation_alias=AliasChoices("for_nodes", "forNodes"),
    )

    for_zones: Annotated[
        list[V1ForZone], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="forZones",
        validation_alias=AliasChoices("for_zones", "forZones"),
    )
