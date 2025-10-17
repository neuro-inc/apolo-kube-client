from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1HostIP",)


class V1HostIP(BaseModel):
    ip: str | None = Field(default=None)
