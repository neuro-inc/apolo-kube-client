from pydantic import BaseModel, Field


class V2MetricTarget(BaseModel):
    average_utilization: int | None = Field(None, alias="averageUtilization")

    average_value: str | None = Field(None, alias="averageValue")

    type: str | None = Field(None, alias="type")

    value: str | None = Field(None, alias="value")
