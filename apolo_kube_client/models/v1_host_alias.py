from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1HostAlias",)


class V1HostAlias(BaseModel):
    hostnames: list[str] = Field(default_factory=lambda: [])

    ip: str | None = Field(default_factory=lambda: None)
