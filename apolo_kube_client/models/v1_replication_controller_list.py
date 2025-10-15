from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1_replication_controller import V1ReplicationController


class V1ReplicationControllerList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1ReplicationController] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
