from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_node_config_source import V1NodeConfigSource

__all__ = ("V1NodeConfigStatus",)


class V1NodeConfigStatus(BaseModel):
    active: V1NodeConfigSource | None = Field(None, alias="active")

    assigned: V1NodeConfigSource | None = Field(None, alias="assigned")

    error: str | None = Field(None, alias="error")

    last_known_good: V1NodeConfigSource | None = Field(None, alias="lastKnownGood")
