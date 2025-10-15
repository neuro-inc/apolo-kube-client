from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_self_subject_access_review_spec import V1SelfSubjectAccessReviewSpec
from .v1_subject_access_review_status import V1SubjectAccessReviewStatus


class V1SelfSubjectAccessReview(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1SelfSubjectAccessReviewSpec | None = Field(None, alias="spec")

    status: V1SubjectAccessReviewStatus | None = Field(None, alias="status")
