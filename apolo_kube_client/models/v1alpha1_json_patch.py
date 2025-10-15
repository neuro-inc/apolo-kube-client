from pydantic import BaseModel, Field


class V1alpha1JSONPatch(BaseModel):
    expression: str | None = Field(None, alias="expression")
