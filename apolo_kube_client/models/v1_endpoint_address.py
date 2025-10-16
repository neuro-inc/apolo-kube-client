from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_reference import V1ObjectReference

__all__ = ("V1EndpointAddress",)


class V1EndpointAddress(BaseModel):
    hostname: str | None = Field(default_factory=lambda: None, alias="hostname")

    ip: str | None = Field(default_factory=lambda: None, alias="ip")

    node_name: str | None = Field(default_factory=lambda: None, alias="nodeName")

    target_ref: V1ObjectReference = Field(
        default_factory=lambda: V1ObjectReference(), alias="targetRef"
    )
