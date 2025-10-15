from pydantic import BaseModel, Field

from .v1_custom_resource_definition import V1CustomResourceDefinition
from .v1_list_meta import V1ListMeta


class V1CustomResourceDefinitionList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    items: list[V1CustomResourceDefinition] | None = Field(None, alias="items")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ListMeta | None = Field(None, alias="metadata")
