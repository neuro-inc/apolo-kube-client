from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1IngressPortStatus",)


class V1IngressPortStatus(BaseModel):
    error: str | None = Field(default=None)

    port: int | None = Field(default=None)

    protocol: str | None = Field(default=None)
