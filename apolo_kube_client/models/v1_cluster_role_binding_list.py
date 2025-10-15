from pydantic import BaseModel, Field

from .v1_cluster_role_binding import V1ClusterRoleBinding
from .v1_list_meta import V1ListMeta


class V1ClusterRoleBindingList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1ClusterRoleBinding] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
