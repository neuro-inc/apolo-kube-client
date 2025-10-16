from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1beta1_self_subject_review_status import V1beta1SelfSubjectReviewStatus

__all__ = ("V1beta1SelfSubjectReview",)


class V1beta1SelfSubjectReview(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    status: V1beta1SelfSubjectReviewStatus | None = Field(None, alias="status")
