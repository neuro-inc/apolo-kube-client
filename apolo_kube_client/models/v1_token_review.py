from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_token_review_spec import V1TokenReviewSpec
from .v1_token_review_status import V1TokenReviewStatus

__all__ = ("V1TokenReview",)


class V1TokenReview(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V1TokenReviewSpec = Field(
        default_factory=lambda: V1TokenReviewSpec(), alias="spec"
    )

    status: V1TokenReviewStatus = Field(
        default_factory=lambda: V1TokenReviewStatus(), alias="status"
    )
