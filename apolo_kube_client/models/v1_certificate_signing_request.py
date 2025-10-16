from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_certificate_signing_request_spec import V1CertificateSigningRequestSpec
from .v1_certificate_signing_request_status import V1CertificateSigningRequestStatus
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1CertificateSigningRequest",)


class V1CertificateSigningRequest(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V1CertificateSigningRequestSpec = Field(
        default_factory=lambda: V1CertificateSigningRequestSpec(), alias="spec"
    )

    status: V1CertificateSigningRequestStatus = Field(
        default_factory=lambda: V1CertificateSigningRequestStatus(), alias="status"
    )
