from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("StorageV1TokenRequest",)


class StorageV1TokenRequest(BaseModel):
    audience: str | None = Field(default=None)

    expiration_seconds: int | None = Field(
        default=None,
        serialization_alias="expirationSeconds",
        validation_alias=AliasChoices("expiration_seconds", "expirationSeconds"),
    )
