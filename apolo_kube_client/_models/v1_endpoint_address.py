from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_object_reference import V1ObjectReference
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1EndpointAddress",)


class V1EndpointAddress(BaseModel):
    hostname: str | None = None

    ip: str | None = None

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
