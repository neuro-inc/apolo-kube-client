from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1_stateful_set import V1StatefulSet


class V1StatefulSetList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1StatefulSet] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
