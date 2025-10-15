from datetime import datetime

from pydantic import BaseModel, Field

from .core_v1_event_series import CoreV1EventSeries
from .v1_event_source import V1EventSource
from .v1_object_meta import V1ObjectMeta
from .v1_object_reference import V1ObjectReference


class CoreV1Event(BaseModel):
    action: str | None = Field(None, alias="action")

    api_version: str | None = Field(None, alias="apiVersion")

    count: int | None = Field(None, alias="count")

    event_time: datetime | None = Field(None, alias="eventTime")

    first_timestamp: datetime | None = Field(None, alias="firstTimestamp")

    involved_object: V1ObjectReference | None = Field(None, alias="involvedObject")

    kind: str | None = Field(None, alias="kind")

    last_timestamp: datetime | None = Field(None, alias="lastTimestamp")

    message: str | None = Field(None, alias="message")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    reason: str | None = Field(None, alias="reason")

    related: V1ObjectReference | None = Field(None, alias="related")

    reporting_component: str | None = Field(None, alias="reportingComponent")

    reporting_instance: str | None = Field(None, alias="reportingInstance")

    series: CoreV1EventSeries | None = Field(None, alias="series")

    source: V1EventSource | None = Field(None, alias="source")

    type: str | None = Field(None, alias="type")
