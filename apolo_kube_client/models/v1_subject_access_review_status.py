from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1SubjectAccessReviewStatus",)


class V1SubjectAccessReviewStatus(BaseModel):
    allowed: bool | None = None

    denied: bool | None = None

    evaluation_error: str | None = Field(
        default=None,
        serialization_alias="evaluationError",
        validation_alias=AliasChoices("evaluation_error", "evaluationError"),
    )

    reason: str | None = None
