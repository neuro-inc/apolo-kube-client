from pydantic import AliasChoices, Field
from .base import ListModel
from .v1_cluster_role_binding import V1ClusterRoleBinding
from .v1_list_meta import V1ListMeta

__all__ = ("V1ClusterRoleBindingList",)


class V1ClusterRoleBindingList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1ClusterRoleBinding] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
