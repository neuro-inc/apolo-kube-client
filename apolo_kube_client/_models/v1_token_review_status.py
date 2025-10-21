from pydantic import BaseModel, Field
from .base import _default_if_none
from .v1_user_info import V1UserInfo
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1TokenReviewStatus",)


class V1TokenReviewStatus(BaseModel):
    audiences: list[str] = []

    authenticated: bool | None = None

    error: str | None = None

    user: Annotated[V1UserInfo, BeforeValidator(_default_if_none(V1UserInfo))] = Field(
        default_factory=lambda: V1UserInfo()
    )
