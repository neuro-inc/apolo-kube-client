from pydantic import BaseModel, Field

from .admissionregistration_v1_service_reference import (
    AdmissionregistrationV1ServiceReference,
)


class AdmissionregistrationV1WebhookClientConfig(BaseModel):
    ca_bundle: str | None = Field(None, alias="caBundle")

    service: AdmissionregistrationV1ServiceReference | None = Field(
        None, alias="service"
    )

    url: str | None = Field(None, alias="url")
