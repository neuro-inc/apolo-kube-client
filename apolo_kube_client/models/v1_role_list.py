from pydantic import BaseModel, Field

from .v1_list_meta import V1ListMeta
from .v1_role import V1Role


class V1RoleList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1Role] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
