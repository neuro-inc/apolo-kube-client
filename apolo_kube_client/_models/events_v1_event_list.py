from pydantic import AliasChoices, Field
from .base import ListModel
from .events_v1_event import EventsV1Event
from .v1_list_meta import V1ListMeta

__all__ = ("EventsV1EventList",)


class EventsV1EventList(ListModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[EventsV1Event] = []

    kind: str | None = None

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
