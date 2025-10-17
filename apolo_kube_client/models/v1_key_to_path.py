from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1KeyToPath",)


class V1KeyToPath(BaseModel):
    key: str | None = Field(default=None)

    mode: int | None = Field(default=None)

    path: str | None = Field(default=None)
