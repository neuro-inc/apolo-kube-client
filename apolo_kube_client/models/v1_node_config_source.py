from pydantic import BaseModel, Field

from .v1_config_map_node_config_source import V1ConfigMapNodeConfigSource


class V1NodeConfigSource(BaseModel):
    config_map: V1ConfigMapNodeConfigSource | None = Field(None, alias="configMap")
