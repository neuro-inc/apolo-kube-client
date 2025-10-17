from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1PortStatus",)


class V1PortStatus(BaseModel):
    error: str | None = Field(default_factory=lambda: None)

    port: int | None = Field(default_factory=lambda: None)

    protocol: str | None = Field(default_factory=lambda: None)
