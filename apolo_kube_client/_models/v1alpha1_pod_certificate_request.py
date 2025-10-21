from pydantic import AliasChoices, Field
from .base import ResourceModel
from .base import _default_if_none
from .v1_object_meta import V1ObjectMeta
from .v1alpha1_pod_certificate_request_spec import V1alpha1PodCertificateRequestSpec
from .v1alpha1_pod_certificate_request_status import V1alpha1PodCertificateRequestStatus
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1alpha1PodCertificateRequest",)


class V1alpha1PodCertificateRequest(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    spec: Annotated[
        V1alpha1PodCertificateRequestSpec,
        BeforeValidator(_default_if_none(V1alpha1PodCertificateRequestSpec)),
    ] = Field(default_factory=lambda: V1alpha1PodCertificateRequestSpec())

    status: Annotated[
        V1alpha1PodCertificateRequestStatus,
        BeforeValidator(_default_if_none(V1alpha1PodCertificateRequestStatus)),
    ] = Field(default_factory=lambda: V1alpha1PodCertificateRequestStatus())
