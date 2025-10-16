from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1HTTPHeader",)


class V1HTTPHeader(BaseModel):
    name: str | None = Field(None, alias="name")

    value: str | None = Field(None, alias="value")
