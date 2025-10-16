from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1TokenReviewSpec",)


class V1TokenReviewSpec(BaseModel):
    audiences: list[str] | None = Field(None, alias="audiences")

    token: str | None = Field(None, alias="token")
