from pydantic import BaseModel
from .v1_certificate_signing_request_condition import (
    V1CertificateSigningRequestCondition,
)

__all__ = ("V1CertificateSigningRequestStatus",)


class V1CertificateSigningRequestStatus(BaseModel):
    certificate: str | None = None

    conditions: list[V1CertificateSigningRequestCondition] = []
