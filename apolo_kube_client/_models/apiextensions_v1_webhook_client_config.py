from pydantic import AliasChoices, BaseModel, Field
from .apiextensions_v1_service_reference import ApiextensionsV1ServiceReference

__all__ = ("ApiextensionsV1WebhookClientConfig",)


class ApiextensionsV1WebhookClientConfig(BaseModel):
    ca_bundle: str | None = Field(
        default=None,
        serialization_alias="caBundle",
        validation_alias=AliasChoices("ca_bundle", "caBundle"),
    )

    service: ApiextensionsV1ServiceReference = Field(
        default_factory=lambda: ApiextensionsV1ServiceReference()
    )

    url: str | None = None
