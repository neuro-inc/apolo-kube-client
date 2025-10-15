from pydantic import BaseModel, Field


class V1alpha1MatchCondition(BaseModel):
    expression: str | None = Field(None, alias="expression")

    name: str | None = Field(None, alias="name")
