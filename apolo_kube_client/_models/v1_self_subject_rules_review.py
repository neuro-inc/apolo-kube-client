from pydantic import AliasChoices, Field
from .base import ResourceModel
from .base import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_self_subject_rules_review_spec import V1SelfSubjectRulesReviewSpec
from .v1_subject_rules_review_status import V1SubjectRulesReviewStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1SelfSubjectRulesReview",)


class V1SelfSubjectRulesReview(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: Annotated[
        V1SelfSubjectRulesReviewSpec,
        BeforeValidator(_default_if_none(V1SelfSubjectRulesReviewSpec)),
    ] = Field(default_factory=lambda: V1SelfSubjectRulesReviewSpec())

    status: Annotated[
        V1SubjectRulesReviewStatus,
        BeforeValidator(_default_if_none(V1SubjectRulesReviewStatus)),
    ] = Field(default_factory=lambda: V1SubjectRulesReviewStatus())
