from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1_validating_webhook_configuration import V1ValidatingWebhookConfiguration

__all__ = ("V1ValidatingWebhookConfigurationList",)


class V1ValidatingWebhookConfigurationList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1ValidatingWebhookConfiguration] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
