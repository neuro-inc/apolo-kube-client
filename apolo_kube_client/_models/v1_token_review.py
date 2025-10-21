from pydantic import AliasChoices, Field
from .base import ResourceModel
from .base import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1_token_review_spec import V1TokenReviewSpec
from .v1_token_review_status import V1TokenReviewStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1TokenReview",)


class V1TokenReview(ResourceModel):
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
        V1TokenReviewSpec, BeforeValidator(_default_if_none(V1TokenReviewSpec))
    ] = Field(default_factory=lambda: V1TokenReviewSpec())

    status: Annotated[
        V1TokenReviewStatus, BeforeValidator(_default_if_none(V1TokenReviewStatus))
    ] = Field(default_factory=lambda: V1TokenReviewStatus())
