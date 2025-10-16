from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ServiceBackendPort",)


class V1ServiceBackendPort(BaseModel):
    name: str | None = Field(default_factory=lambda: None, alias="name")

    number: int | None = Field(default_factory=lambda: None, alias="number")
