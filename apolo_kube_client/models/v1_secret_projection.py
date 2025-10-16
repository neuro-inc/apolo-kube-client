from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_key_to_path import V1KeyToPath

__all__ = ("V1SecretProjection",)


class V1SecretProjection(BaseModel):
    items: list[V1KeyToPath] | None = Field(None, alias="items")

    name: str | None = Field(None, alias="name")

    optional: bool | None = Field(None, alias="optional")
