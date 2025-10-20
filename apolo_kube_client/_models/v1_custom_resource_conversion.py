from pydantic import BaseModel, Field
from .v1_webhook_conversion import V1WebhookConversion

__all__ = ("V1CustomResourceConversion",)


class V1CustomResourceConversion(BaseModel):
    strategy: str | None = None

    webhook: V1WebhookConversion = Field(default_factory=lambda: V1WebhookConversion())
