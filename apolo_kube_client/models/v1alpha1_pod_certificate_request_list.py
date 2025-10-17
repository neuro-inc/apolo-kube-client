from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1alpha1_pod_certificate_request import V1alpha1PodCertificateRequest

__all__ = ("V1alpha1PodCertificateRequestList",)


class V1alpha1PodCertificateRequestList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[V1alpha1PodCertificateRequest] = Field(default_factory=lambda: [])

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
