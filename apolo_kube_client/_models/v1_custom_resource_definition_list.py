from pydantic import AliasChoices, Field
from .base import ListModel
from .base import _default_if_none
from .v1_custom_resource_definition import V1CustomResourceDefinition
from .v1_list_meta import V1ListMeta
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CustomResourceDefinitionList",)


class V1CustomResourceDefinitionList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1CustomResourceDefinition] = []

    kind: str | None = None

    metadata: Annotated[V1ListMeta, BeforeValidator(_default_if_none(V1ListMeta))] = (
        Field(default_factory=lambda: V1ListMeta())
    )
