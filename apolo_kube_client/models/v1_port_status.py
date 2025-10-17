from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1PortStatus",)


class V1PortStatus(BaseModel):
    error: str | None = Field(default=None)

    port: int | None = Field(default=None)

    protocol: str | None = Field(default=None)
