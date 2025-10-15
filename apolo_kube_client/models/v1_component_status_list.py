from pydantic import BaseModel, Field

from .v1_component_status import V1ComponentStatus
from .v1_list_meta import V1ListMeta


class V1ComponentStatusList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1ComponentStatus] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
