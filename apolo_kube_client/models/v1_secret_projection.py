from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_key_to_path import V1KeyToPath

__all__ = ("V1SecretProjection",)


class V1SecretProjection(BaseModel):
    items: list[V1KeyToPath] = Field(default=[])

    name: str | None = Field(default=None)

    optional: bool | None = Field(default=None)
