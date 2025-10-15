from pydantic import BaseModel, Field

from .v1_mutating_webhook import V1MutatingWebhook
from .v1_object_meta import V1ObjectMeta


class V1MutatingWebhookConfiguration(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    webhooks: list[V1MutatingWebhook] | None = Field(None, alias="webhooks")
