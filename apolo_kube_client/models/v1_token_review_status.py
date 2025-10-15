from pydantic import BaseModel, Field

from .v1_user_info import V1UserInfo


class V1TokenReviewStatus(BaseModel):
    audiences: list[str] | None = Field(None, alias="audiences")

    authenticated: bool | None = Field(None, alias="authenticated")

    error: str | None = Field(None, alias="error")

    user: V1UserInfo | None = Field(None, alias="user")
