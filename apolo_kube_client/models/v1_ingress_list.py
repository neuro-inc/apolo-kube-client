from pydantic import BaseModel, Field

from .v1_ingress import V1Ingress
from .v1_list_meta import V1ListMeta


class V1IngressList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1Ingress] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
