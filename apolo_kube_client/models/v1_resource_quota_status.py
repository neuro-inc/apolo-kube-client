from pydantic import BaseModel, Field


class V1ResourceQuotaStatus(BaseModel):
    hard: dict(str, str) | None = Field(None, alias="hard")

    used: dict(str, str) | None = Field(None, alias="used")
