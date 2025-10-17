from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1SELinuxOptions",)


class V1SELinuxOptions(BaseModel):
    level: str | None = Field(default=None)

    role: str | None = Field(default=None)

    type: str | None = Field(default=None)

    user: str | None = Field(default=None)
