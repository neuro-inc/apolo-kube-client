from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1UserSubject",)


class V1UserSubject(BaseModel):
    name: str | None = Field(None, alias="name")
