from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1SubjectAccessReviewStatus",)


class V1SubjectAccessReviewStatus(BaseModel):
    allowed: bool | None = Field(default_factory=lambda: None, alias="allowed")

    denied: bool | None = Field(default_factory=lambda: None, alias="denied")

    evaluation_error: str | None = Field(
        default_factory=lambda: None, alias="evaluationError"
    )

    reason: str | None = Field(default_factory=lambda: None, alias="reason")
