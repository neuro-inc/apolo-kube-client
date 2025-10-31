from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_cluster_trust_bundle_projection import V1ClusterTrustBundleProjection
from .v1_config_map_projection import V1ConfigMapProjection
from .v1_downward_api_projection import V1DownwardAPIProjection
from .v1_pod_certificate_projection import V1PodCertificateProjection
from .v1_secret_projection import V1SecretProjection
from .v1_service_account_token_projection import V1ServiceAccountTokenProjection
from pydantic import BeforeValidator

__all__ = ("V1VolumeProjection",)


class V1VolumeProjection(BaseModel):
    """Projection that may be projected along with other supported volume types. Exactly one of these fields must be set."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.VolumeProjection"

    cluster_trust_bundle: Annotated[
        V1ClusterTrustBundleProjection | None,
        Field(
            alias="clusterTrustBundle",
            description="""ClusterTrustBundle allows a pod to access the `.spec.trustBundle` field of ClusterTrustBundle objects in an auto-updating file.

Alpha, gated by the ClusterTrustBundleProjection feature gate.

ClusterTrustBundle objects can either be selected by name, or by the combination of signer name and a label selector.

Kubelet performs aggressive normalization of the PEM contents written into the pod filesystem.  Esoteric PEM features such as inter-block comments and block headers are stripped.  Certificates are deduplicated. The ordering of certificates within the file is arbitrary, and Kubelet may change the order over time.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    config_map: Annotated[
        V1ConfigMapProjection,
        Field(
            alias="configMap",
            description="""configMap information about the configMap data to project""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ConfigMapProjection)),
    ] = V1ConfigMapProjection()

    downward_api: Annotated[
        V1DownwardAPIProjection,
        Field(
            alias="downwardAPI",
            description="""downwardAPI information about the downwardAPI data to project""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1DownwardAPIProjection)),
    ] = V1DownwardAPIProjection()

    pod_certificate: Annotated[
        V1PodCertificateProjection | None,
        Field(
            alias="podCertificate",
            description="""Projects an auto-rotating credential bundle (private key and certificate chain) that the pod can use either as a TLS client or server.

Kubelet generates a private key and uses it to send a PodCertificateRequest to the named signer.  Once the signer approves the request and issues a certificate chain, Kubelet writes the key and certificate chain to the pod filesystem.  The pod does not start until certificates have been issued for each podCertificate projected volume source in its spec.

Kubelet will begin trying to rotate the certificate at the time indicated by the signer using the PodCertificateRequest.Status.BeginRefreshAt timestamp.

Kubelet can write a single file, indicated by the credentialBundlePath field, or separate files, indicated by the keyPath and certificateChainPath fields.

The credential bundle is a single file in PEM format.  The first PEM entry is the private key (in PKCS#8 format), and the remaining PEM entries are the certificate chain issued by the signer (typically, signers will return their certificate chain in leaf-to-root order).

Prefer using the credential bundle format, since your application code can read it atomically.  If you use keyPath and certificateChainPath, your application must make two separate file reads. If these coincide with a certificate rotation, it is possible that the private key and leaf certificate you read may not correspond to each other.  Your application will need to check for this condition, and re-read until they are consistent.

The named signer controls chooses the format of the certificate it issues; consult the signer implementation's documentation to learn how to use the certificates it issues.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    secret: Annotated[
        V1SecretProjection,
        Field(
            description="""secret information about the secret data to project""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1SecretProjection)),
    ] = V1SecretProjection()

    service_account_token: Annotated[
        V1ServiceAccountTokenProjection | None,
        Field(
            alias="serviceAccountToken",
            description="""serviceAccountToken is information about the serviceAccountToken data to project""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
