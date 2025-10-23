from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_object_meta import V1ObjectMeta
from .v1_self_subject_access_review_spec import V1SelfSubjectAccessReviewSpec
from .v1_subject_access_review_status import V1SubjectAccessReviewStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1SelfSubjectAccessReview",)


class V1SelfSubjectAccessReview(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
        exclude_if=_exclude_if,
    )

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta(), exclude_if=_exclude_if)

    spec: Annotated[
        V1SelfSubjectAccessReviewSpec,
        BeforeValidator(_default_if_none(V1SelfSubjectAccessReviewSpec)),
    ] = Field(
        default_factory=lambda: V1SelfSubjectAccessReviewSpec(), exclude_if=_exclude_if
    )

    status: Annotated[
        V1SubjectAccessReviewStatus,
        BeforeValidator(_default_if_none(V1SubjectAccessReviewStatus)),
    ] = Field(
        default_factory=lambda: V1SubjectAccessReviewStatus(), exclude_if=_exclude_if
    )
