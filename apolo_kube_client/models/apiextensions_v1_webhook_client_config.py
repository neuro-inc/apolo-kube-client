from __future__ import annotations

from pydantic import BaseModel, Field

from .apiextensions_v1_service_reference import ApiextensionsV1ServiceReference

__all__ = ("ApiextensionsV1WebhookClientConfig",)


class ApiextensionsV1WebhookClientConfig(BaseModel):
    ca_bundle: str | None = Field(None, alias="caBundle")

    service: ApiextensionsV1ServiceReference | None = Field(None, alias="service")

    url: str | None = Field(None, alias="url")
