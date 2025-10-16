from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1GRPCAction",)


class V1GRPCAction(BaseModel):
    port: int | None = Field(None, alias="port")

    service: str | None = Field(None, alias="service")
