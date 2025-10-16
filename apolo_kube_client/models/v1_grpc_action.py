from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1GRPCAction",)


class V1GRPCAction(BaseModel):
    port: int | None = Field(default_factory=lambda: None, alias="port")

    service: str | None = Field(default_factory=lambda: None, alias="service")
