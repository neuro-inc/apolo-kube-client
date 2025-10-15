from pydantic import BaseModel, Field


class V1beta1ExpressionWarning(BaseModel):
    field_ref: str | None = Field(None, alias="fieldRef")

    warning: str | None = Field(None, alias="warning")
