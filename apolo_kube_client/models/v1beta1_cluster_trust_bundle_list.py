from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1beta1_cluster_trust_bundle import V1beta1ClusterTrustBundle

__all__ = ("V1beta1ClusterTrustBundleList",)


class V1beta1ClusterTrustBundleList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[V1beta1ClusterTrustBundle] = Field(
        default_factory=lambda: [], alias="items"
    )

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta(), alias="metadata")
