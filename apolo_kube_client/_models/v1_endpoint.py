from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_endpoint_conditions import V1EndpointConditions
from .v1_endpoint_hints import V1EndpointHints
from .v1_object_reference import V1ObjectReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1Endpoint",)


class V1Endpoint(BaseModel):
    addresses: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[], exclude_if=_exclude_if
    )

    conditions: Annotated[
        V1EndpointConditions, BeforeValidator(_default_if_none(V1EndpointConditions))
    ] = Field(default_factory=lambda: V1EndpointConditions(), exclude_if=_exclude_if)

    deprecated_topology: Annotated[
        dict[str, str], BeforeValidator(_collection_if_none("{}"))
    ] = Field(
        default={},
        serialization_alias="deprecatedTopology",
        validation_alias=AliasChoices("deprecated_topology", "deprecatedTopology"),
        exclude_if=_exclude_if,
    )

    hints: Annotated[
        V1EndpointHints, BeforeValidator(_default_if_none(V1EndpointHints))
    ] = Field(default_factory=lambda: V1EndpointHints(), exclude_if=_exclude_if)

    hostname: str | None = Field(default=None, exclude_if=_exclude_if)

    node_name: str | None = Field(
        default=None,
        serialization_alias="nodeName",
        validation_alias=AliasChoices("node_name", "nodeName"),
        exclude_if=_exclude_if,
    )

    target_ref: Annotated[
        V1ObjectReference, BeforeValidator(_default_if_none(V1ObjectReference))
    ] = Field(
        default_factory=lambda: V1ObjectReference(),
        serialization_alias="targetRef",
        validation_alias=AliasChoices("target_ref", "targetRef"),
        exclude_if=_exclude_if,
    )

    zone: str | None = Field(default=None, exclude_if=_exclude_if)
