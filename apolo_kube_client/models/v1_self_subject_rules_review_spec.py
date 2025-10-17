from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1SelfSubjectRulesReviewSpec",)


class V1SelfSubjectRulesReviewSpec(BaseModel):
    namespace: str | None = Field(default=None)
