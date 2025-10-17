from __future__ import annotations
from pydantic import BaseModel, Field
from .apiextensions_v1_service_reference import ApiextensionsV1ServiceReference

__all__ = ("ApiextensionsV1WebhookClientConfig",)


class ApiextensionsV1WebhookClientConfig(BaseModel):
    ca_bundle: str | None = Field(default_factory=lambda: None, alias="caBundle")

    service: ApiextensionsV1ServiceReference = Field(
        default_factory=lambda: ApiextensionsV1ServiceReference()
    )

    url: str | None = Field(default_factory=lambda: None)
