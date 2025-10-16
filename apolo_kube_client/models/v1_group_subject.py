from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1GroupSubject",)


class V1GroupSubject(BaseModel):
    name: str | None = Field(None, alias="name")
