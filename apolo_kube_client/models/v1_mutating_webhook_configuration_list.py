from pydantic import AliasChoices, Field
from .base import ListModel
from .v1_list_meta import V1ListMeta
from .v1_mutating_webhook_configuration import V1MutatingWebhookConfiguration

__all__ = ("V1MutatingWebhookConfigurationList",)


class V1MutatingWebhookConfigurationList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1MutatingWebhookConfiguration] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
