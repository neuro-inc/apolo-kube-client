from pydantic import BaseModel, Field

from .v1_daemon_set import V1DaemonSet
from .v1_list_meta import V1ListMeta


class V1DaemonSetList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1DaemonSet] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
