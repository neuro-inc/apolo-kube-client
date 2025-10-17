from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_self_subject_review_status import V1SelfSubjectReviewStatus

__all__ = ("V1SelfSubjectReview",)


class V1SelfSubjectReview(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    status: V1SelfSubjectReviewStatus = Field(
        default_factory=lambda: V1SelfSubjectReviewStatus()
    )
