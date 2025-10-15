from pydantic import BaseModel, Field


class V1SubjectAccessReviewStatus(BaseModel):
    allowed: bool | None = Field(None, alias="allowed")

    denied: bool | None = Field(None, alias="denied")

    evaluation_error: str | None = Field(None, alias="evaluationError")

    reason: str | None = Field(None, alias="reason")
