from pydantic import BaseModel, Field

from .v1_ingress_class import V1IngressClass
from .v1_list_meta import V1ListMeta


class V1IngressClassList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1IngressClass] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
