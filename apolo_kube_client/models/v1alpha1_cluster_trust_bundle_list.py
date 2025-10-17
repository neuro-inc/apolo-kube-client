from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1alpha1_cluster_trust_bundle import V1alpha1ClusterTrustBundle

__all__ = ("V1alpha1ClusterTrustBundleList",)


class V1alpha1ClusterTrustBundleList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1alpha1ClusterTrustBundle] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
