from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1ConfigMap",)


class V1ConfigMap(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    binary_data: dict[str, str] = Field(default_factory=lambda: {}, alias="binaryData")

    data: dict[str, str] = Field(default_factory=lambda: {})

    immutable: bool | None = Field(default_factory=lambda: None)

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())
