from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_node_selector import V1NodeSelector

__all__ = ("V1VolumeNodeAffinity",)


class V1VolumeNodeAffinity(BaseModel):
    required: V1NodeSelector = Field(
        default_factory=lambda: V1NodeSelector(), alias="required"
    )
