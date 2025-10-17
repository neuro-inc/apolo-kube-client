from __future__ import annotations
from pydantic import BaseModel, Field
from .events_v1_event_series import EventsV1EventSeries
from .v1_event_source import V1EventSource
from .v1_object_meta import V1ObjectMeta
from .v1_object_reference import V1ObjectReference
from datetime import datetime

__all__ = ("EventsV1Event",)


class EventsV1Event(BaseModel):
    action: str | None = Field(default_factory=lambda: None)

    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    deprecated_count: int | None = Field(
        default_factory=lambda: None, alias="deprecatedCount"
    )

    deprecated_first_timestamp: datetime | None = Field(
        default_factory=lambda: None, alias="deprecatedFirstTimestamp"
    )

    deprecated_last_timestamp: datetime | None = Field(
        default_factory=lambda: None, alias="deprecatedLastTimestamp"
    )

    deprecated_source: V1EventSource = Field(
        default_factory=lambda: V1EventSource(), alias="deprecatedSource"
    )

    event_time: datetime | None = Field(default_factory=lambda: None, alias="eventTime")

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    note: str | None = Field(default_factory=lambda: None)

    reason: str | None = Field(default_factory=lambda: None)

    regarding: V1ObjectReference = Field(default_factory=lambda: V1ObjectReference())

    related: V1ObjectReference = Field(default_factory=lambda: V1ObjectReference())

    reporting_controller: str | None = Field(
        default_factory=lambda: None, alias="reportingController"
    )

    reporting_instance: str | None = Field(
        default_factory=lambda: None, alias="reportingInstance"
    )

    series: EventsV1EventSeries = Field(default_factory=lambda: EventsV1EventSeries())

    type: str | None = Field(default_factory=lambda: None)
