from pydantic import AliasChoices, BaseModel, Field
from .admissionregistration_v1_service_reference import (
    AdmissionregistrationV1ServiceReference,
)
from .base import _default_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("AdmissionregistrationV1WebhookClientConfig",)


class AdmissionregistrationV1WebhookClientConfig(BaseModel):
    ca_bundle: str | None = Field(
        default=None,
        serialization_alias="caBundle",
        validation_alias=AliasChoices("ca_bundle", "caBundle"),
    )

    service: Annotated[
        AdmissionregistrationV1ServiceReference,
        BeforeValidator(_default_if_none(AdmissionregistrationV1ServiceReference)),
    ] = Field(default_factory=lambda: AdmissionregistrationV1ServiceReference())

    url: str | None = None
