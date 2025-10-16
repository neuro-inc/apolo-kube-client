from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

__all__ = ("V1TokenRequestStatus",)


class V1TokenRequestStatus(BaseModel):
    expiration_timestamp: datetime | None = Field(None, alias="expirationTimestamp")

    token: str | None = Field(None, alias="token")
