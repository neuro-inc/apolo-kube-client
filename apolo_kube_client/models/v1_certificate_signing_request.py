from pydantic import BaseModel, Field

from .v1_certificate_signing_request_spec import V1CertificateSigningRequestSpec
from .v1_certificate_signing_request_status import V1CertificateSigningRequestStatus
from .v1_object_meta import V1ObjectMeta


class V1CertificateSigningRequest(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1CertificateSigningRequestSpec | None = Field(None, alias="spec")

    status: V1CertificateSigningRequestStatus | None = Field(None, alias="status")
