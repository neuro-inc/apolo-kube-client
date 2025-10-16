from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1EndpointConditions",)


class V1EndpointConditions(BaseModel):
    ready: bool | None = Field(default_factory=lambda: None, alias="ready")

    serving: bool | None = Field(default_factory=lambda: None, alias="serving")

    terminating: bool | None = Field(default_factory=lambda: None, alias="terminating")
