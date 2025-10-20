from pydantic import AliasChoices, Field
from .base import ResourceModel
from .v1_object_meta import V1ObjectMeta
from .v1_token_review_spec import V1TokenReviewSpec
from .v1_token_review_status import V1TokenReviewStatus

__all__ = ("V1TokenReview",)


class V1TokenReview(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1TokenReviewSpec = Field(default_factory=lambda: V1TokenReviewSpec())

    status: V1TokenReviewStatus = Field(default_factory=lambda: V1TokenReviewStatus())
