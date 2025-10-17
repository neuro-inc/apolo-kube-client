from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from datetime import datetime

__all__ = ("V1TokenRequestStatus",)


class V1TokenRequestStatus(BaseModel):
    expiration_timestamp: datetime | None = Field(
        default=None,
        serialization_alias="expirationTimestamp",
        validation_alias=AliasChoices("expiration_timestamp", "expirationTimestamp"),
    )

    token: str | None = Field(default=None)
