from pydantic import AliasChoices, BaseModel, Field
from .v1_certificate_signing_request_spec import V1CertificateSigningRequestSpec
from .v1_certificate_signing_request_status import V1CertificateSigningRequestStatus
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1CertificateSigningRequest",)


class V1CertificateSigningRequest(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1CertificateSigningRequestSpec = Field(
        default_factory=lambda: V1CertificateSigningRequestSpec()
    )

    status: V1CertificateSigningRequestStatus = Field(
        default_factory=lambda: V1CertificateSigningRequestStatus()
    )
