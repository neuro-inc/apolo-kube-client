from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ConfigMapKeySelector",)


class V1ConfigMapKeySelector(BaseModel):
    key: str | None = Field(default=None)

    name: str | None = Field(default=None)

    optional: bool | None = Field(default=None)
