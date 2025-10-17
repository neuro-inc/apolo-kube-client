from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1EndpointConditions",)


class V1EndpointConditions(BaseModel):
    ready: bool | None = Field(default_factory=lambda: None)

    serving: bool | None = Field(default_factory=lambda: None)

    terminating: bool | None = Field(default_factory=lambda: None)
