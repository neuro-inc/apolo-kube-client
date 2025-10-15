from pydantic import BaseModel, Field


class V1ClientIPConfig(BaseModel):
    timeout_seconds: int | None = Field(None, alias="timeoutSeconds")
