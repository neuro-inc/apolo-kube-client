from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_user_info import V1UserInfo
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1SelfSubjectReviewStatus",)


class V1SelfSubjectReviewStatus(BaseModel):
    user_info: Annotated[V1UserInfo, BeforeValidator(_default_if_none(V1UserInfo))] = (
        Field(
            default_factory=lambda: V1UserInfo(),
            serialization_alias="userInfo",
            validation_alias=AliasChoices("user_info", "userInfo"),
        )
    )
