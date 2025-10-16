from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1UserInfo",)


class V1UserInfo(BaseModel):
    extra: dict[str, list[str]] | None = Field(None, alias="extra")

    groups: list[str] | None = Field(None, alias="groups")

    uid: str | None = Field(None, alias="uid")

    username: str | None = Field(None, alias="username")
