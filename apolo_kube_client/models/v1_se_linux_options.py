from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1SELinuxOptions",)


class V1SELinuxOptions(BaseModel):
    level: str | None = Field(default_factory=lambda: None)

    role: str | None = Field(default_factory=lambda: None)

    type: str | None = Field(default_factory=lambda: None)

    user: str | None = Field(default_factory=lambda: None)
