from pydantic import BaseModel, Field


class V1beta1DeviceCapacity(BaseModel):
    value: str | None = Field(None, alias="value")
