from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1alpha1_pod_certificate_request_spec import V1alpha1PodCertificateRequestSpec
from .v1alpha1_pod_certificate_request_status import V1alpha1PodCertificateRequestStatus

__all__ = ("V1alpha1PodCertificateRequest",)


class V1alpha1PodCertificateRequest(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1alpha1PodCertificateRequestSpec = Field(
        default_factory=lambda: V1alpha1PodCertificateRequestSpec()
    )

    status: V1alpha1PodCertificateRequestStatus = Field(
        default_factory=lambda: V1alpha1PodCertificateRequestStatus()
    )
