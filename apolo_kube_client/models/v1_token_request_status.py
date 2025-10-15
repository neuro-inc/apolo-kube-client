from datetime import datetime

from pydantic import BaseModel, Field


class V1TokenRequestStatus(BaseModel):
    expiration_timestamp: datetime | None = Field(None, alias="expirationTimestamp")

    token: str | None = Field(None, alias="token")
