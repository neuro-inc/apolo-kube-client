from pydantic import BaseModel, Field


class V1alpha3CELDeviceSelector(BaseModel):
    expression: str | None = Field(None, alias="expression")
