from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_self_subject_review_status import V1SelfSubjectReviewStatus


class V1SelfSubjectReview(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    status: V1SelfSubjectReviewStatus | None = Field(None, alias="status")
