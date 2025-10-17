from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_cluster_role import V1ClusterRole
from .v1_list_meta import V1ListMeta

__all__ = ("V1ClusterRoleList",)


class V1ClusterRoleList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[V1ClusterRole] = Field(default_factory=lambda: [])

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
