from pydantic import BaseModel, Field


class StorageV1TokenRequest(BaseModel):
    audience: str | None = Field(None, alias="audience")

    expiration_seconds: int | None = Field(None, alias="expirationSeconds")
