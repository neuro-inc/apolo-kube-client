from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_user_info import V1UserInfo

__all__ = ("V1SelfSubjectReviewStatus",)


class V1SelfSubjectReviewStatus(BaseModel):
    user_info: V1UserInfo = Field(
        default_factory=lambda: V1UserInfo(), alias="userInfo"
    )
