from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1UserInfo",)


class V1UserInfo(BaseModel):
    extra: dict[str, list[str]] = Field(default={})

    groups: list[str] = Field(default=[])

    uid: str | None = Field(default=None)

    username: str | None = Field(default=None)
