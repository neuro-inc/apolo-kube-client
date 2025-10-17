from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_node_config_source import V1NodeConfigSource

__all__ = ("V1NodeConfigStatus",)


class V1NodeConfigStatus(BaseModel):
    active: V1NodeConfigSource = Field(default_factory=lambda: V1NodeConfigSource())

    assigned: V1NodeConfigSource = Field(default_factory=lambda: V1NodeConfigSource())

    error: str | None = Field(default_factory=lambda: None)

    last_known_good: V1NodeConfigSource = Field(
        default_factory=lambda: V1NodeConfigSource(), alias="lastKnownGood"
    )
