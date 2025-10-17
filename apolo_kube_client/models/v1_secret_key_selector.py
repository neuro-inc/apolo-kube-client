from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1SecretKeySelector",)


class V1SecretKeySelector(BaseModel):
    key: str | None = Field(default=None)

    name: str | None = Field(default=None)

    optional: bool | None = Field(default=None)
