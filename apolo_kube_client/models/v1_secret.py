from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta

__all__ = ("V1Secret",)


class V1Secret(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    data: dict[str, str] | None = Field(None, alias="data")

    immutable: bool | None = Field(None, alias="immutable")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    string_data: dict[str, str] | None = Field(None, alias="stringData")

    type: str | None = Field(None, alias="type")
