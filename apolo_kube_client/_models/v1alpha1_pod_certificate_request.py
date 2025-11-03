from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ResourceModel
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1alpha1_pod_certificate_request_spec import V1alpha1PodCertificateRequestSpec
from .v1alpha1_pod_certificate_request_status import V1alpha1PodCertificateRequestStatus
from pydantic import BeforeValidator

__all__ = ("V1alpha1PodCertificateRequest",)


class V1alpha1PodCertificateRequest(ResourceModel):
    """PodCertificateRequest encodes a pod requesting a certificate from a given signer.

    Kubelets use this API to implement podCertificate projected volumes"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.certificates.v1alpha1.PodCertificateRequest"
    )

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="certificates.k8s.io", kind="PodCertificateRequest", version="v1alpha1"
    )

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "certificates.k8s.io/v1alpha1"

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "PodCertificateRequest"

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""metadata contains the object metadata.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()

    spec: Annotated[
        V1alpha1PodCertificateRequestSpec,
        Field(
            description="""spec contains the details about the certificate being requested."""
        ),
    ]

    status: Annotated[
        V1alpha1PodCertificateRequestStatus,
        Field(
            description="""status contains the issued certificate, and a standard set of conditions.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1alpha1PodCertificateRequestStatus)),
    ] = V1alpha1PodCertificateRequestStatus()
