from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1beta1ClusterTrustBundleSpec",)


class V1beta1ClusterTrustBundleSpec(BaseModel):
    """ClusterTrustBundleSpec contains the signer and trust anchors."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.certificates.v1beta1.ClusterTrustBundleSpec"
    )

    signer_name: Annotated[
        str | None,
        Field(
            alias="signerName",
            description="""signerName indicates the associated signer, if any.

In order to create or update a ClusterTrustBundle that sets signerName, you must have the following cluster-scoped permission: group=certificates.k8s.io resource=signers resourceName=<the signer name> verb=attest.

If signerName is not empty, then the ClusterTrustBundle object must be named with the signer name as a prefix (translating slashes to colons). For example, for the signer name `example.com/foo`, valid ClusterTrustBundle object names include `example.com:foo:abc` and `example.com:foo:v1`.

If signerName is empty, then the ClusterTrustBundle object's name must not have such a prefix.

List/watch requests for ClusterTrustBundles can filter on this field using a `spec.signerName=NAME` field selector.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    trust_bundle: Annotated[
        str,
        Field(
            alias="trustBundle",
            description="""trustBundle contains the individual X.509 trust anchors for this bundle, as PEM bundle of PEM-wrapped, DER-formatted X.509 certificates.

The data must consist only of PEM certificate blocks that parse as valid X.509 certificates.  Each certificate must include a basic constraints extension with the CA bit set.  The API server will reject objects that contain duplicate certificates, or that use PEM block headers.

Users of ClusterTrustBundles, including Kubelet, are free to reorder and deduplicate certificate blocks in this file according to their own logic, as well as to drop PEM block headers and inter-block data.""",
        ),
    ]
