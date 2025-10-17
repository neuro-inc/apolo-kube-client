from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1_validating_webhook_configuration import V1ValidatingWebhookConfiguration

__all__ = ("V1ValidatingWebhookConfigurationList",)


class V1ValidatingWebhookConfigurationList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1ValidatingWebhookConfiguration] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
