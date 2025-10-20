from pydantic import AliasChoices, Field
from .base import ListModel
from .v1_list_meta import V1ListMeta
from .v1beta1_cluster_trust_bundle import V1beta1ClusterTrustBundle

__all__ = ("V1beta1ClusterTrustBundleList",)


class V1beta1ClusterTrustBundleList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1beta1ClusterTrustBundle] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
