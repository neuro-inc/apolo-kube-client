from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1SELinuxOptions",)


class V1SELinuxOptions(BaseModel):
    level: str | None = Field(default_factory=lambda: None, alias="level")

    role: str | None = Field(default_factory=lambda: None, alias="role")

    type: str | None = Field(default_factory=lambda: None, alias="type")

    user: str | None = Field(default_factory=lambda: None, alias="user")
