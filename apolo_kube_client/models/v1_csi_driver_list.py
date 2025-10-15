from pydantic import BaseModel, Field

from .v1_c_s_i_driver import V1CSIDriver
from .v1_list_meta import V1ListMeta


class V1CSIDriverList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1CSIDriver] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
