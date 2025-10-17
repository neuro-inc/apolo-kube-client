from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1TokenReviewSpec",)


class V1TokenReviewSpec(BaseModel):
    audiences: list[str] = Field(default_factory=lambda: [])

    token: str | None = Field(default_factory=lambda: None)
