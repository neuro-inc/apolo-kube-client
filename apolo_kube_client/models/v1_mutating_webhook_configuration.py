from pydantic import AliasChoices, BaseModel, Field
from .v1_mutating_webhook import V1MutatingWebhook
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1MutatingWebhookConfiguration",)


class V1MutatingWebhookConfiguration(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    webhooks: list[V1MutatingWebhook] = []
