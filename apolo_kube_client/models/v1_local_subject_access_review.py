from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_subject_access_review_spec import V1SubjectAccessReviewSpec
from .v1_subject_access_review_status import V1SubjectAccessReviewStatus


class V1LocalSubjectAccessReview(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1SubjectAccessReviewSpec | None = Field(None, alias="spec")

    status: V1SubjectAccessReviewStatus | None = Field(None, alias="status")
