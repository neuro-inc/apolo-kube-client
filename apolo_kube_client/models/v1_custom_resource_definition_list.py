from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_custom_resource_definition import V1CustomResourceDefinition
from .v1_list_meta import V1ListMeta

__all__ = ("V1CustomResourceDefinitionList",)


class V1CustomResourceDefinitionList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[V1CustomResourceDefinition] = Field(
        default_factory=lambda: [], alias="items"
    )

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta(), alias="metadata")
