from pydantic import BaseModel, Field

from .v1_user_info import V1UserInfo


class V1beta1SelfSubjectReviewStatus(BaseModel):
    user_info: V1UserInfo | None = Field(None, alias="userInfo")
