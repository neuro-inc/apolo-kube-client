from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1beta1MatchCondition",)


class V1beta1MatchCondition(BaseModel):
    expression: str | None = Field(default_factory=lambda: None)

    name: str | None = Field(default_factory=lambda: None)
