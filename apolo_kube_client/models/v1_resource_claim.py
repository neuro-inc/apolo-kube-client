from pydantic import BaseModel, Field


class V1ResourceClaim(BaseModel):
    name: str | None = Field(None, alias="name")

    request: str | None = Field(None, alias="request")
