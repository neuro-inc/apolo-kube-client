from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_cluster_role_binding import V1ClusterRoleBinding
from .v1_list_meta import V1ListMeta

__all__ = ("V1ClusterRoleBindingList",)


class V1ClusterRoleBindingList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[V1ClusterRoleBinding] = Field(default_factory=lambda: [], alias="items")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta(), alias="metadata")
