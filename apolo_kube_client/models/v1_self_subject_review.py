from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_self_subject_review_status import V1SelfSubjectReviewStatus

__all__ = ("V1SelfSubjectReview",)


class V1SelfSubjectReview(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    status: V1SelfSubjectReviewStatus = Field(
        default_factory=lambda: V1SelfSubjectReviewStatus(), alias="status"
    )
