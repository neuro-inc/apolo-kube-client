from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_validating_webhook import V1ValidatingWebhook

__all__ = ("V1ValidatingWebhookConfiguration",)


class V1ValidatingWebhookConfiguration(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    webhooks: list[V1ValidatingWebhook] = Field(default=[])
