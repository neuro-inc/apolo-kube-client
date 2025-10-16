from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1DaemonEndpoint",)


class V1DaemonEndpoint(BaseModel):
    port: int | None = Field(None, alias="Port")
