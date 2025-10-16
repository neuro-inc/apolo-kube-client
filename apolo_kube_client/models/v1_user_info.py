from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1UserInfo",)


class V1UserInfo(BaseModel):
    extra: dict[str, list[str]] = Field(default_factory=lambda: {}, alias="extra")

    groups: list[str] = Field(default_factory=lambda: [], alias="groups")

    uid: str | None = Field(default_factory=lambda: None, alias="uid")

    username: str | None = Field(default_factory=lambda: None, alias="username")
