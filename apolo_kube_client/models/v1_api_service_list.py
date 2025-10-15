from pydantic import BaseModel, Field

from .v1_a_p_i_service import V1APIService
from .v1_list_meta import V1ListMeta


class V1APIServiceList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1APIService] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
