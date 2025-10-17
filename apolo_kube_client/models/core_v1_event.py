from __future__ import annotations
from pydantic import BaseModel, Field
from .core_v1_event_series import CoreV1EventSeries
from .v1_event_source import V1EventSource
from .v1_object_meta import V1ObjectMeta
from .v1_object_reference import V1ObjectReference
from datetime import datetime

__all__ = ("CoreV1Event",)


class CoreV1Event(BaseModel):
    action: str | None = Field(default_factory=lambda: None)

    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    count: int | None = Field(default_factory=lambda: None)

    event_time: datetime | None = Field(default_factory=lambda: None, alias="eventTime")

    first_timestamp: datetime | None = Field(
        default_factory=lambda: None, alias="firstTimestamp"
    )

    involved_object: V1ObjectReference = Field(
        default_factory=lambda: V1ObjectReference(), alias="involvedObject"
    )

    kind: str | None = Field(default_factory=lambda: None)

    last_timestamp: datetime | None = Field(
        default_factory=lambda: None, alias="lastTimestamp"
    )

    message: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    reason: str | None = Field(default_factory=lambda: None)

    related: V1ObjectReference = Field(default_factory=lambda: V1ObjectReference())

    reporting_component: str | None = Field(
        default_factory=lambda: None, alias="reportingComponent"
    )

    reporting_instance: str | None = Field(
        default_factory=lambda: None, alias="reportingInstance"
    )

    series: CoreV1EventSeries = Field(default_factory=lambda: CoreV1EventSeries())

    source: V1EventSource = Field(default_factory=lambda: V1EventSource())

    type: str | None = Field(default_factory=lambda: None)
