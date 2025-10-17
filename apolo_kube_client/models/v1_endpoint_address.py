from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_object_reference import V1ObjectReference

__all__ = ("V1EndpointAddress",)


class V1EndpointAddress(BaseModel):
    hostname: str | None = Field(default=None)

    ip: str | None = Field(default=None)

    node_name: str | None = Field(
        default=None,
        serialization_alias="nodeName",
        validation_alias=AliasChoices("node_name", "nodeName"),
    )

    target_ref: V1ObjectReference = Field(
        default_factory=lambda: V1ObjectReference(),
        serialization_alias="targetRef",
        validation_alias=AliasChoices("target_ref", "targetRef"),
    )
