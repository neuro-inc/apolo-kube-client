from pydantic import AliasChoices, Field
from .base import ResourceModel
from .utils import _default_if_none
from .utils import _exclude_if
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
        exclude_if=_exclude_if,
    )

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta(), exclude_if=_exclude_if)

    spec: Annotated[
        V1alpha1PodCertificateRequestSpec,
        BeforeValidator(_default_if_none(V1alpha1PodCertificateRequestSpec)),
    ] = Field(
        default_factory=lambda: V1alpha1PodCertificateRequestSpec(),
        exclude_if=_exclude_if,
    )

    status: Annotated[
        V1alpha1PodCertificateRequestStatus,
        BeforeValidator(_default_if_none(V1alpha1PodCertificateRequestStatus)),
    ] = Field(
        default_factory=lambda: V1alpha1PodCertificateRequestStatus(),
        exclude_if=_exclude_if,
    )
