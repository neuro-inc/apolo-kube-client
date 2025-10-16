from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1EndpointConditions",)


class V1EndpointConditions(BaseModel):
    ready: bool | None = Field(None, alias="ready")

    serving: bool | None = Field(None, alias="serving")

    terminating: bool | None = Field(None, alias="terminating")
