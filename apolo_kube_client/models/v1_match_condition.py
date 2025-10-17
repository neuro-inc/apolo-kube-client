from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1MatchCondition",)


class V1MatchCondition(BaseModel):
    expression: str | None = Field(default=None)

    name: str | None = Field(default=None)
