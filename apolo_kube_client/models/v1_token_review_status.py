from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_user_info import V1UserInfo

__all__ = ("V1TokenReviewStatus",)


class V1TokenReviewStatus(BaseModel):
    audiences: list[str] = Field(default=[])

    authenticated: bool | None = Field(default=None)

    error: str | None = Field(default=None)

    user: V1UserInfo = Field(default_factory=lambda: V1UserInfo())
