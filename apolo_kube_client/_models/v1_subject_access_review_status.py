from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if

__all__ = ("V1SubjectAccessReviewStatus",)


class V1SubjectAccessReviewStatus(BaseModel):
    allowed: bool | None = Field(default=None, exclude_if=_exclude_if)

    denied: bool | None = Field(default=None, exclude_if=_exclude_if)

    evaluation_error: str | None = Field(
        default=None,
        serialization_alias="evaluationError",
        validation_alias=AliasChoices("evaluation_error", "evaluationError"),
        exclude_if=_exclude_if,
    )

    reason: str | None = Field(default=None, exclude_if=_exclude_if)
