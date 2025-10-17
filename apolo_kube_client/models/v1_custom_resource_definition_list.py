from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_custom_resource_definition import V1CustomResourceDefinition
from .v1_list_meta import V1ListMeta

__all__ = ("V1CustomResourceDefinitionList",)


class V1CustomResourceDefinitionList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1CustomResourceDefinition] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
