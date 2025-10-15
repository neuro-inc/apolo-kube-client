from pydantic import BaseModel, Field

from .v1_webhook_conversion import V1WebhookConversion


class V1CustomResourceConversion(BaseModel):
    strategy: str | None = Field(None, alias="strategy")

    webhook: V1WebhookConversion | None = Field(None, alias="webhook")
