from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_config_map import V1ConfigMap
from .v1_list_meta import V1ListMeta

__all__ = ("V1ConfigMapList",)


class V1ConfigMapList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[V1ConfigMap] = Field(default_factory=lambda: [], alias="items")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta(), alias="metadata")
