from pydantic import BaseModel, Field


class V1alpha1ApplyConfiguration(BaseModel):
    expression: str | None = Field(None, alias="expression")
