from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1HostAlias",)


class V1HostAlias(BaseModel):
    hostnames: list[str] | None = Field(None, alias="hostnames")

    ip: str | None = Field(None, alias="ip")
