from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_validating_webhook import V1ValidatingWebhook


class V1ValidatingWebhookConfiguration(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    webhooks: list[V1ValidatingWebhook] | None = Field(None, alias="webhooks")
