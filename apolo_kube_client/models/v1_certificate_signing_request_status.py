from pydantic import BaseModel, Field

from .v1_certificate_signing_request_condition import (
    V1CertificateSigningRequestCondition,
)


class V1CertificateSigningRequestStatus(BaseModel):
    certificate: str | None = Field(None, alias="certificate")

    conditions: list[V1CertificateSigningRequestCondition] | None = Field(
        None, alias="conditions"
    )
