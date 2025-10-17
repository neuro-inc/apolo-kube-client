from pydantic import AliasChoices, BaseModel, Field
from .apiextensions_v1_webhook_client_config import ApiextensionsV1WebhookClientConfig

__all__ = ("V1WebhookConversion",)


class V1WebhookConversion(BaseModel):
    client_config: ApiextensionsV1WebhookClientConfig = Field(
        default_factory=lambda: ApiextensionsV1WebhookClientConfig(),
        serialization_alias="clientConfig",
        validation_alias=AliasChoices("client_config", "clientConfig"),
    )

    conversion_review_versions: list[str] = Field(
        default=[],
        serialization_alias="conversionReviewVersions",
        validation_alias=AliasChoices(
            "conversion_review_versions", "conversionReviewVersions"
        ),
    )
