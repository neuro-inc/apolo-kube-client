from __future__ import annotations
from pydantic import BaseModel, Field
from .admissionregistration_v1_service_reference import (
    AdmissionregistrationV1ServiceReference,
)

__all__ = ("AdmissionregistrationV1WebhookClientConfig",)


class AdmissionregistrationV1WebhookClientConfig(BaseModel):
    ca_bundle: str | None = Field(default_factory=lambda: None, alias="caBundle")

    service: AdmissionregistrationV1ServiceReference = Field(
        default_factory=lambda: AdmissionregistrationV1ServiceReference()
    )

    url: str | None = Field(default_factory=lambda: None)
