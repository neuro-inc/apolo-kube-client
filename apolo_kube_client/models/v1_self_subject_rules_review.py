from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_self_subject_rules_review_spec import V1SelfSubjectRulesReviewSpec
from .v1_subject_rules_review_status import V1SubjectRulesReviewStatus


class V1SelfSubjectRulesReview(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1SelfSubjectRulesReviewSpec | None = Field(None, alias="spec")

    status: V1SubjectRulesReviewStatus | None = Field(None, alias="status")
