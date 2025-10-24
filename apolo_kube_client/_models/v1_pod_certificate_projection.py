from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1PodCertificateProjection",)


class V1PodCertificateProjection(BaseModel):
    """PodCertificateProjection provides a private key and X.509 certificate in the pod filesystem."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.PodCertificateProjection"

    certificate_chain_path: Annotated[
        str | None,
        Field(
            alias="certificateChainPath",
            description="""Write the certificate chain at this path in the projected volume.

Most applications should use credentialBundlePath.  When using keyPath and certificateChainPath, your application needs to check that the key and leaf certificate are consistent, because it is possible to read the files mid-rotation.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    credential_bundle_path: Annotated[
        str | None,
        Field(
            alias="credentialBundlePath",
            description="""Write the credential bundle at this path in the projected volume.

The credential bundle is a single file that contains multiple PEM blocks. The first PEM block is a PRIVATE KEY block, containing a PKCS#8 private key.

The remaining blocks are CERTIFICATE blocks, containing the issued certificate chain from the signer (leaf and any intermediates).

Using credentialBundlePath lets your Pod's application code make a single atomic read that retrieves a consistent key and certificate chain.  If you project them to separate files, your application code will need to additionally check that the leaf certificate was issued to the key.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    key_path: Annotated[
        str | None,
        Field(
            alias="keyPath",
            description="""Write the key at this path in the projected volume.

Most applications should use credentialBundlePath.  When using keyPath and certificateChainPath, your application needs to check that the key and leaf certificate are consistent, because it is possible to read the files mid-rotation.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    key_type: Annotated[
        str,
        Field(
            alias="keyType",
            description="""The type of keypair Kubelet will generate for the pod.

Valid values are "RSA3072", "RSA4096", "ECDSAP256", "ECDSAP384", "ECDSAP521", and "ED25519".""",
        ),
    ]

    max_expiration_seconds: Annotated[
        int | None,
        Field(
            alias="maxExpirationSeconds",
            description="""maxExpirationSeconds is the maximum lifetime permitted for the certificate.

Kubelet copies this value verbatim into the PodCertificateRequests it generates for this projection.

If omitted, kube-apiserver will set it to 86400(24 hours). kube-apiserver will reject values shorter than 3600 (1 hour).  The maximum allowable value is 7862400 (91 days).

The signer implementation is then free to issue a certificate with any lifetime *shorter* than MaxExpirationSeconds, but no shorter than 3600 seconds (1 hour).  This constraint is enforced by kube-apiserver. `kubernetes.io` signers will never issue certificates with a lifetime longer than 24 hours.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    signer_name: Annotated[
        str,
        Field(
            alias="signerName",
            description="""Kubelet's generated CSRs will be addressed to this signer.""",
        ),
    ]
