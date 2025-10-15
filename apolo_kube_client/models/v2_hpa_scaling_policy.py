from pydantic import BaseModel, Field


class V2HPAScalingPolicy(BaseModel):
    period_seconds: int | None = Field(None, alias="periodSeconds")

    type: str | None = Field(None, alias="type")

    value: int | None = Field(None, alias="value")
