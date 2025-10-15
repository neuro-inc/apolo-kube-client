from pydantic import BaseModel, Field

from .v1_endpoints import V1Endpoints
from .v1_list_meta import V1ListMeta


class V1EndpointsList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1Endpoints] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
