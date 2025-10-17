from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1KeyToPath",)


class V1KeyToPath(BaseModel):
    key: str | None = Field(default_factory=lambda: None)

    mode: int | None = Field(default_factory=lambda: None)

    path: str | None = Field(default_factory=lambda: None)
