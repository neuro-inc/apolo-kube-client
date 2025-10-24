from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_for_node import V1ForNode
from .v1_for_zone import V1ForZone
from pydantic import BeforeValidator

__all__ = ("V1EndpointHints",)


class V1EndpointHints(BaseModel):
    """EndpointHints provides hints describing how an endpoint should be consumed."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.discovery.v1.EndpointHints"

    for_nodes: Annotated[
        list[V1ForNode],
        Field(
            alias="forNodes",
            description="""forNodes indicates the node(s) this endpoint should be consumed by when using topology aware routing. May contain a maximum of 8 entries. This is an Alpha feature and is only used when the PreferSameTrafficDistribution feature gate is enabled.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    for_zones: Annotated[
        list[V1ForZone],
        Field(
            alias="forZones",
            description="""forZones indicates the zone(s) this endpoint should be consumed by when using topology aware routing. May contain a maximum of 8 entries.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
