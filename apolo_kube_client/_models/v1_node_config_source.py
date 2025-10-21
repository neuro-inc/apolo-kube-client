from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .v1_config_map_node_config_source import V1ConfigMapNodeConfigSource
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1NodeConfigSource",)


class V1NodeConfigSource(BaseModel):
    config_map: Annotated[
        V1ConfigMapNodeConfigSource,
        BeforeValidator(_default_if_none(V1ConfigMapNodeConfigSource)),
    ] = Field(
        default_factory=lambda: V1ConfigMapNodeConfigSource(),
        serialization_alias="configMap",
        validation_alias=AliasChoices("config_map", "configMap"),
    )
