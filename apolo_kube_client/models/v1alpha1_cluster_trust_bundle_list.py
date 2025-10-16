from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1alpha1_cluster_trust_bundle import V1alpha1ClusterTrustBundle

__all__ = ("V1alpha1ClusterTrustBundleList",)


class V1alpha1ClusterTrustBundleList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1alpha1ClusterTrustBundle] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
