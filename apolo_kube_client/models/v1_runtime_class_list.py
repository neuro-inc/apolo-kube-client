from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1_runtime_class import V1RuntimeClass

__all__ = ("V1RuntimeClassList",)


class V1RuntimeClassList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1RuntimeClass] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
