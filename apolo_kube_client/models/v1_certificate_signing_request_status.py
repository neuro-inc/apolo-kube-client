from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_certificate_signing_request_condition import (
    V1CertificateSigningRequestCondition,
)

__all__ = ("V1CertificateSigningRequestStatus",)


class V1CertificateSigningRequestStatus(BaseModel):
    certificate: str | None = Field(default=None)

    conditions: list[V1CertificateSigningRequestCondition] = Field(default=[])
