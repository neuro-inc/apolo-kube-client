from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_mutating_webhook import V1MutatingWebhook
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1MutatingWebhookConfiguration",)


class V1MutatingWebhookConfiguration(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    webhooks: list[V1MutatingWebhook] = Field(default_factory=lambda: [])
