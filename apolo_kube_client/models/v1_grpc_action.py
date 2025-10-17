from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1GRPCAction",)


class V1GRPCAction(BaseModel):
    port: int | None = Field(default=None)

    service: str | None = Field(default=None)
