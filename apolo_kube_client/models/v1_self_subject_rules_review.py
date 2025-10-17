from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_self_subject_rules_review_spec import V1SelfSubjectRulesReviewSpec
from .v1_subject_rules_review_status import V1SubjectRulesReviewStatus

__all__ = ("V1SelfSubjectRulesReview",)


class V1SelfSubjectRulesReview(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1SelfSubjectRulesReviewSpec = Field(
        default_factory=lambda: V1SelfSubjectRulesReviewSpec()
    )

    status: V1SubjectRulesReviewStatus = Field(
        default_factory=lambda: V1SubjectRulesReviewStatus()
    )
