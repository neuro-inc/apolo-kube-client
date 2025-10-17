from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_config_map_node_config_source import V1ConfigMapNodeConfigSource

__all__ = ("V1NodeConfigSource",)


class V1NodeConfigSource(BaseModel):
    config_map: V1ConfigMapNodeConfigSource = Field(
        default_factory=lambda: V1ConfigMapNodeConfigSource(),
        serialization_alias="configMap",
        validation_alias=AliasChoices("config_map", "configMap"),
    )
