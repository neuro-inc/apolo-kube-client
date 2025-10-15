from pydantic import BaseModel, Field


class V1ExpressionWarning(BaseModel):
    field_ref: str | None = Field(None, alias="fieldRef")

    warning: str | None = Field(None, alias="warning")
