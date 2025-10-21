from pydantic import AliasChoices, Field
from .base import ResourceModel
from .base import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_subject_access_review_spec import V1SubjectAccessReviewSpec
from .v1_subject_access_review_status import V1SubjectAccessReviewStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1LocalSubjectAccessReview",)


class V1LocalSubjectAccessReview(ResourceModel):
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
        V1SubjectAccessReviewSpec,
        BeforeValidator(_default_if_none(V1SubjectAccessReviewSpec)),
    ] = Field(default_factory=lambda: V1SubjectAccessReviewSpec())

    status: Annotated[
        V1SubjectAccessReviewStatus,
        BeforeValidator(_default_if_none(V1SubjectAccessReviewStatus)),
    ] = Field(default_factory=lambda: V1SubjectAccessReviewStatus())
