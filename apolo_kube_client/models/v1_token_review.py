from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_token_review_spec import V1TokenReviewSpec
from .v1_token_review_status import V1TokenReviewStatus

__all__ = ("V1TokenReview",)


class V1TokenReview(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1TokenReviewSpec | None = Field(None, alias="spec")

    status: V1TokenReviewStatus | None = Field(None, alias="status")
