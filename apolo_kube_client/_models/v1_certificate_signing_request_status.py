from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_certificate_signing_request_condition import (
    V1CertificateSigningRequestCondition,
)
from pydantic import BeforeValidator

__all__ = ("V1CertificateSigningRequestStatus",)


class V1CertificateSigningRequestStatus(BaseModel):
    """CertificateSigningRequestStatus contains conditions used to indicate approved/denied/failed status of the request, and the issued certificate."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.certificates.v1.CertificateSigningRequestStatus"
    )

    certificate: Annotated[
        str | None,
        Field(
            description="""certificate is populated with an issued certificate by the signer after an Approved condition is present. This field is set via the /status subresource. Once populated, this field is immutable.

If the certificate signing request is denied, a condition of type "Denied" is added and this field remains empty. If the signer cannot issue the certificate, a condition of type "Failed" is added and this field remains empty.

Validation requirements:
 1. certificate must contain one or more PEM blocks.
 2. All PEM blocks must have the "CERTIFICATE" label, contain no headers, and the encoded data
  must be a BER-encoded ASN.1 Certificate structure as described in section 4 of RFC5280.
 3. Non-PEM content may appear before or after the "CERTIFICATE" PEM blocks and is unvalidated,
  to allow for explanatory text as described in section 5.2 of RFC7468.

If more than one PEM block is present, and the definition of the requested spec.signerName does not indicate otherwise, the first block is the issued certificate, and subsequent blocks should be treated as intermediate certificates and presented in TLS handshakes.

The certificate is encoded in PEM format.

When serialized as JSON or YAML, the data is additionally base64-encoded, so it consists of:

    base64(
    -----BEGIN CERTIFICATE-----
    ...
    -----END CERTIFICATE-----
    )""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    conditions: Annotated[
        list[V1CertificateSigningRequestCondition],
        Field(
            description="""conditions applied to the request. Known conditions are "Approved", "Denied", and "Failed".""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
