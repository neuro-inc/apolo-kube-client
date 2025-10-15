from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1_node import V1Node


class V1NodeList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1Node] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
