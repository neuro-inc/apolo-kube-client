from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_object_reference import V1ObjectReference

__all__ = ("V1Binding",)


class V1Binding(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    target: V1ObjectReference = Field(default_factory=lambda: V1ObjectReference())
