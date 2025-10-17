from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_cluster_role_binding import V1ClusterRoleBinding
from .v1_list_meta import V1ListMeta

__all__ = ("V1ClusterRoleBindingList",)


class V1ClusterRoleBindingList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1ClusterRoleBinding] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
