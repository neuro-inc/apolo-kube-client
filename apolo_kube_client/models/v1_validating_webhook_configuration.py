from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_validating_webhook import V1ValidatingWebhook

__all__ = ("V1ValidatingWebhookConfiguration",)


class V1ValidatingWebhookConfiguration(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    webhooks: list[V1ValidatingWebhook] = Field(
        default_factory=lambda: [], alias="webhooks"
    )
