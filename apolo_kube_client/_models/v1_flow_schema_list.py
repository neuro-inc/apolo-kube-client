from pydantic import AliasChoices, Field
from .base import ListModel
from .v1_flow_schema import V1FlowSchema
from .v1_list_meta import V1ListMeta

__all__ = ("V1FlowSchemaList",)


class V1FlowSchemaList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1FlowSchema] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
