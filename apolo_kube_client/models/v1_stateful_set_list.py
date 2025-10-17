from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_list_meta import V1ListMeta
from .v1_stateful_set import V1StatefulSet

__all__ = ("V1StatefulSetList",)


class V1StatefulSetList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1StatefulSet] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
