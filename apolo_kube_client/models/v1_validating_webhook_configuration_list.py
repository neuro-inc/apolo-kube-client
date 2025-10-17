from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1_validating_webhook_configuration import V1ValidatingWebhookConfiguration

__all__ = ("V1ValidatingWebhookConfigurationList",)


class V1ValidatingWebhookConfigurationList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[V1ValidatingWebhookConfiguration] = Field(default_factory=lambda: [])

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
