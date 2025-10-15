from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1_service import V1Service


class V1ServiceList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1Service] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
