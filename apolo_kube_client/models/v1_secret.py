from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1Secret",)


class V1Secret(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    data: dict[str, str] = Field(default_factory=lambda: {}, alias="data")

    immutable: bool | None = Field(default_factory=lambda: None, alias="immutable")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    string_data: dict[str, str] = Field(default_factory=lambda: {}, alias="stringData")

    type: str | None = Field(default_factory=lambda: None, alias="type")
