from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1_mutating_webhook_configuration import V1MutatingWebhookConfiguration

__all__ = ("V1MutatingWebhookConfigurationList",)


class V1MutatingWebhookConfigurationList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[V1MutatingWebhookConfiguration] = Field(default_factory=lambda: [])

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
