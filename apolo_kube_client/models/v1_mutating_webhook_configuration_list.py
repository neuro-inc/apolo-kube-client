from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1_mutating_webhook_configuration import V1MutatingWebhookConfiguration

__all__ = ("V1MutatingWebhookConfigurationList",)


class V1MutatingWebhookConfigurationList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1MutatingWebhookConfiguration] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
