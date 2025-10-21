from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_endpoint_conditions import V1EndpointConditions
from .v1_endpoint_hints import V1EndpointHints
from .v1_object_reference import V1ObjectReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1Endpoint",)


class V1Endpoint(BaseModel):
    addresses: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []

    conditions: Annotated[
        V1EndpointConditions, BeforeValidator(_default_if_none(V1EndpointConditions))
    ] = Field(default_factory=lambda: V1EndpointConditions())

    deprecated_topology: Annotated[
        dict[str, str], BeforeValidator(_collection_if_none("{}"))
    ] = Field(
        default={},
        serialization_alias="deprecatedTopology",
        validation_alias=AliasChoices("deprecated_topology", "deprecatedTopology"),
    )

    hints: Annotated[
        V1EndpointHints, BeforeValidator(_default_if_none(V1EndpointHints))
    ] = Field(default_factory=lambda: V1EndpointHints())

    hostname: str | None = None

    node_name: str | None = Field(
        default=None,
        serialization_alias="nodeName",
        validation_alias=AliasChoices("node_name", "nodeName"),
    )

    target_ref: Annotated[
        V1ObjectReference, BeforeValidator(_default_if_none(V1ObjectReference))
    ] = Field(
        default_factory=lambda: V1ObjectReference(),
        serialization_alias="targetRef",
        validation_alias=AliasChoices("target_ref", "targetRef"),
    )

    zone: str | None = None
