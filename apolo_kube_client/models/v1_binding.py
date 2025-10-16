from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_object_reference import V1ObjectReference

__all__ = ("V1Binding",)


class V1Binding(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    target: V1ObjectReference | None = Field(None, alias="target")
