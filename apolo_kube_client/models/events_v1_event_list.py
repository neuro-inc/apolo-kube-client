from __future__ import annotations
from pydantic import BaseModel, Field
from .events_v1_event import EventsV1Event
from .v1_list_meta import V1ListMeta

__all__ = ("EventsV1EventList",)


class EventsV1EventList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[EventsV1Event] = Field(default_factory=lambda: [])

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
