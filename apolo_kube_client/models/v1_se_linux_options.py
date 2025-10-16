from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1SELinuxOptions",)


class V1SELinuxOptions(BaseModel):
    level: str | None = Field(None, alias="level")

    role: str | None = Field(None, alias="role")

    type: str | None = Field(None, alias="type")

    user: str | None = Field(None, alias="user")
