from pydantic import BaseModel, Field


class V1TokenReviewSpec(BaseModel):
    audiences: list[str] | None = Field(None, alias="audiences")

    token: str | None = Field(None, alias="token")
