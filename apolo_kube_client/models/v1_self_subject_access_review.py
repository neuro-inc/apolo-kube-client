from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_self_subject_access_review_spec import V1SelfSubjectAccessReviewSpec
from .v1_subject_access_review_status import V1SubjectAccessReviewStatus

__all__ = ("V1SelfSubjectAccessReview",)


class V1SelfSubjectAccessReview(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1SelfSubjectAccessReviewSpec = Field(
        default_factory=lambda: V1SelfSubjectAccessReviewSpec()
    )

    status: V1SubjectAccessReviewStatus = Field(
        default_factory=lambda: V1SubjectAccessReviewStatus()
    )
