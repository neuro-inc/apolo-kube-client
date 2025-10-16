from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_component_status import V1ComponentStatus
from .v1_list_meta import V1ListMeta

__all__ = ("V1ComponentStatusList",)


class V1ComponentStatusList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[V1ComponentStatus] = Field(default_factory=lambda: [], alias="items")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta(), alias="metadata")
