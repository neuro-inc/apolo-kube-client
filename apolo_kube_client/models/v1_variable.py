from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1Variable",)


class V1Variable(BaseModel):
    expression: str | None = Field(None, alias="expression")

    name: str | None = Field(None, alias="name")
