from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_node_runtime_handler_features import V1NodeRuntimeHandlerFeatures

__all__ = ("V1NodeRuntimeHandler",)


class V1NodeRuntimeHandler(BaseModel):
    features: V1NodeRuntimeHandlerFeatures = Field(
        default_factory=lambda: V1NodeRuntimeHandlerFeatures()
    )

    name: str | None = Field(default_factory=lambda: None)
