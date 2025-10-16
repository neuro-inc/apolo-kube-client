from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1_mutating_webhook_configuration import V1MutatingWebhookConfiguration

__all__ = ("V1MutatingWebhookConfigurationList",)


class V1MutatingWebhookConfigurationList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1MutatingWebhookConfiguration] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
