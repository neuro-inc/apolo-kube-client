from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1alpha1_cluster_trust_bundle_spec import V1alpha1ClusterTrustBundleSpec

__all__ = ("V1alpha1ClusterTrustBundle",)


class V1alpha1ClusterTrustBundle(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1alpha1ClusterTrustBundleSpec | None = Field(None, alias="spec")
