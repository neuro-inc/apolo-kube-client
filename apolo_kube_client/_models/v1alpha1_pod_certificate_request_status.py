from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_condition import V1Condition
from datetime import datetime
from pydantic import BeforeValidator

__all__ = ("V1alpha1PodCertificateRequestStatus",)


class V1alpha1PodCertificateRequestStatus(BaseModel):
    """PodCertificateRequestStatus describes the status of the request, and holds the certificate data if the request is issued."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.certificates.v1alpha1.PodCertificateRequestStatus"
    )

    begin_refresh_at: Annotated[
        datetime | None,
        Field(
            alias="beginRefreshAt",
            description="""beginRefreshAt is the time at which the kubelet should begin trying to refresh the certificate.  This field is set via the /status subresource, and must be set at the same time as certificateChain.  Once populated, this field is immutable.

This field is only a hint.  Kubelet may start refreshing before or after this time if necessary.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    certificate_chain: Annotated[
        str | None,
        Field(
            alias="certificateChain",
            description="""certificateChain is populated with an issued certificate by the signer. This field is set via the /status subresource. Once populated, this field is immutable.

If the certificate signing request is denied, a condition of type "Denied" is added and this field remains empty. If the signer cannot issue the certificate, a condition of type "Failed" is added and this field remains empty.

Validation requirements:
 1. certificateChain must consist of one or more PEM-formatted certificates.
 2. Each entry must be a valid PEM-wrapped, DER-encoded ASN.1 Certificate as
    described in section 4 of RFC5280.

If more than one block is present, and the definition of the requested spec.signerName does not indicate otherwise, the first block is the issued certificate, and subsequent blocks should be treated as intermediate certificates and presented in TLS handshakes.  When projecting the chain into a pod volume, kubelet will drop any data in-between the PEM blocks, as well as any PEM block headers.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    conditions: Annotated[
        list[V1Condition],
        Field(
            description="""conditions applied to the request.

The types "Issued", "Denied", and "Failed" have special handling.  At most one of these conditions may be present, and they must have status "True".

If the request is denied with `Reason=UnsupportedKeyType`, the signer may suggest a key type that will work in the message field.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    not_after: Annotated[
        datetime | None,
        Field(
            alias="notAfter",
            description="""notAfter is the time at which the certificate expires.  The value must be the same as the notAfter value in the leaf certificate in certificateChain.  This field is set via the /status subresource.  Once populated, it is immutable.  The signer must set this field at the same time it sets certificateChain.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    not_before: Annotated[
        datetime | None,
        Field(
            alias="notBefore",
            description="""notBefore is the time at which the certificate becomes valid.  The value must be the same as the notBefore value in the leaf certificate in certificateChain.  This field is set via the /status subresource.  Once populated, it is immutable. The signer must set this field at the same time it sets certificateChain.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
