from __future__ import annotations

from pydantic import BaseModel, Field

from .apiextensions_v1_webhook_client_config import ApiextensionsV1WebhookClientConfig

__all__ = ("V1WebhookConversion",)


class V1WebhookConversion(BaseModel):
    client_config: ApiextensionsV1WebhookClientConfig | None = Field(
        None, alias="clientConfig"
    )

    conversion_review_versions: list[str] | None = Field(
        None, alias="conversionReviewVersions"
    )
