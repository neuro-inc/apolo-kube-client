from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1_pod import V1Pod


class V1PodList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1Pod] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
