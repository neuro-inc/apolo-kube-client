from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1EventSource",)


class V1EventSource(BaseModel):
    component: str | None = Field(default_factory=lambda: None, alias="component")

    host: str | None = Field(default_factory=lambda: None, alias="host")
