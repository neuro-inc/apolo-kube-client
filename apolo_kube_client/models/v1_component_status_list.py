from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_component_status import V1ComponentStatus
from .v1_list_meta import V1ListMeta

__all__ = ("V1ComponentStatusList",)


class V1ComponentStatusList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1ComponentStatus] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
