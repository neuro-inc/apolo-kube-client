from __future__ import annotations
from pydantic import BaseModel, Field
from .core_v1_event import CoreV1Event
from .v1_list_meta import V1ListMeta

__all__ = ("CoreV1EventList",)


class CoreV1EventList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[CoreV1Event] = Field(default_factory=lambda: [], alias="items")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta(), alias="metadata")
