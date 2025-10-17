from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1alpha1_cluster_trust_bundle_spec import V1alpha1ClusterTrustBundleSpec

__all__ = ("V1alpha1ClusterTrustBundle",)


class V1alpha1ClusterTrustBundle(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1alpha1ClusterTrustBundleSpec = Field(
        default_factory=lambda: V1alpha1ClusterTrustBundleSpec()
    )
