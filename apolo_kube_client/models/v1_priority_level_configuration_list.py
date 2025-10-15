from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1_priority_level_configuration import V1PriorityLevelConfiguration


class V1PriorityLevelConfigurationList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1PriorityLevelConfiguration] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
