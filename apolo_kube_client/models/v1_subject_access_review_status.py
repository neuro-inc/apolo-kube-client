from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1SubjectAccessReviewStatus",)


class V1SubjectAccessReviewStatus(BaseModel):
    allowed: bool | None = Field(default=None)

    denied: bool | None = Field(default=None)

    evaluation_error: str | None = Field(
        default=None,
        serialization_alias="evaluationError",
        validation_alias=AliasChoices("evaluation_error", "evaluationError"),
    )

    reason: str | None = Field(default=None)
