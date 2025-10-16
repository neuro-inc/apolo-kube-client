from __future__ import annotations
from pydantic import BaseModel, Field
from datetime import datetime

__all__ = ("V1TokenRequestStatus",)


class V1TokenRequestStatus(BaseModel):
    expiration_timestamp: datetime | None = Field(
        default_factory=lambda: None, alias="expirationTimestamp"
    )

    token: str | None = Field(default_factory=lambda: None, alias="token")
