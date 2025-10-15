from pydantic import BaseModel, Field


class V1beta1CELDeviceSelector(BaseModel):
    expression: str | None = Field(None, alias="expression")
