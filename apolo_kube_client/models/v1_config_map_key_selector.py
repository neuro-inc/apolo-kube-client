from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1ConfigMapKeySelector",)


class V1ConfigMapKeySelector(BaseModel):
    key: str | None = Field(None, alias="key")

    name: str | None = Field(None, alias="name")

    optional: bool | None = Field(None, alias="optional")
