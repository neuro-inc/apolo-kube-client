from datetime import datetime

from pydantic import BaseModel, Field


class V1Taint(BaseModel):
    effect: str | None = Field(None, alias="effect")

    key: str | None = Field(None, alias="key")

    time_added: datetime | None = Field(None, alias="timeAdded")

    value: str | None = Field(None, alias="value")
