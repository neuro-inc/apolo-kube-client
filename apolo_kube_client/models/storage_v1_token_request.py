from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("StorageV1TokenRequest",)


class StorageV1TokenRequest(BaseModel):
    audience: str | None = Field(None, alias="audience")

    expiration_seconds: int | None = Field(None, alias="expirationSeconds")
