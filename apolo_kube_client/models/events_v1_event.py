from datetime import datetime

from pydantic import BaseModel, Field

from .events_v1_event_series import EventsV1EventSeries
from .v1_event_source import V1EventSource
from .v1_object_meta import V1ObjectMeta
from .v1_object_reference import V1ObjectReference


class EventsV1Event(BaseModel):
    action: str | None = Field(None, alias="action")

    api_version: str | None = Field(None, alias="apiVersion")

    deprecated_count: int | None = Field(None, alias="deprecatedCount")

    deprecated_first_timestamp: datetime | None = Field(
        None, alias="deprecatedFirstTimestamp"
    )

    deprecated_last_timestamp: datetime | None = Field(
        None, alias="deprecatedLastTimestamp"
    )

    deprecated_source: V1EventSource | None = Field(None, alias="deprecatedSource")

    event_time: datetime | None = Field(None, alias="eventTime")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    note: str | None = Field(None, alias="note")

    reason: str | None = Field(None, alias="reason")

    regarding: V1ObjectReference | None = Field(None, alias="regarding")

    related: V1ObjectReference | None = Field(None, alias="related")

    reporting_controller: str | None = Field(None, alias="reportingController")

    reporting_instance: str | None = Field(None, alias="reportingInstance")

    series: EventsV1EventSeries | None = Field(None, alias="series")

    type: str | None = Field(None, alias="type")
