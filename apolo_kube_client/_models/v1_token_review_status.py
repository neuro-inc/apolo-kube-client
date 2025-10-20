from pydantic import BaseModel, Field
from .v1_user_info import V1UserInfo

__all__ = ("V1TokenReviewStatus",)


class V1TokenReviewStatus(BaseModel):
    audiences: list[str] = []

    authenticated: bool | None = None

    error: str | None = None

    user: V1UserInfo = Field(default_factory=lambda: V1UserInfo())
