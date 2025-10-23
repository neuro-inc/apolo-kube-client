from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_object_meta import V1ObjectMeta
from .v1_self_subject_review_status import V1SelfSubjectReviewStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1SelfSubjectReview",)


class V1SelfSubjectReview(ResourceModel):
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

    status: Annotated[
        V1SelfSubjectReviewStatus,
        BeforeValidator(_default_if_none(V1SelfSubjectReviewStatus)),
    ] = Field(
        default_factory=lambda: V1SelfSubjectReviewStatus(), exclude_if=_exclude_if
    )
