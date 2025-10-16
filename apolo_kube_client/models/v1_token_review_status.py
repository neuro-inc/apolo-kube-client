from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_user_info import V1UserInfo

__all__ = ("V1TokenReviewStatus",)


class V1TokenReviewStatus(BaseModel):
    audiences: list[str] = Field(default_factory=lambda: [], alias="audiences")

    authenticated: bool | None = Field(
        default_factory=lambda: None, alias="authenticated"
    )

    error: str | None = Field(default_factory=lambda: None, alias="error")

    user: V1UserInfo = Field(default_factory=lambda: V1UserInfo(), alias="user")
