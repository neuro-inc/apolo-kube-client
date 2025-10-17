from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .events_v1_event_series import EventsV1EventSeries
from .v1_event_source import V1EventSource
from .v1_object_meta import V1ObjectMeta
from .v1_object_reference import V1ObjectReference
from datetime import datetime

__all__ = ("EventsV1Event",)


class EventsV1Event(BaseModel):
    action: str | None = Field(default=None)

    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    deprecated_count: int | None = Field(
        default=None,
        serialization_alias="deprecatedCount",
        validation_alias=AliasChoices("deprecated_count", "deprecatedCount"),
    )

    deprecated_first_timestamp: datetime | None = Field(
        default=None,
        serialization_alias="deprecatedFirstTimestamp",
        validation_alias=AliasChoices(
            "deprecated_first_timestamp", "deprecatedFirstTimestamp"
        ),
    )

    deprecated_last_timestamp: datetime | None = Field(
        default=None,
        serialization_alias="deprecatedLastTimestamp",
        validation_alias=AliasChoices(
            "deprecated_last_timestamp", "deprecatedLastTimestamp"
        ),
    )

    deprecated_source: V1EventSource = Field(
        default_factory=lambda: V1EventSource(),
        serialization_alias="deprecatedSource",
        validation_alias=AliasChoices("deprecated_source", "deprecatedSource"),
    )

    event_time: datetime | None = Field(
        default=None,
        serialization_alias="eventTime",
        validation_alias=AliasChoices("event_time", "eventTime"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    note: str | None = Field(default=None)

    reason: str | None = Field(default=None)

    regarding: V1ObjectReference = Field(default_factory=lambda: V1ObjectReference())

    related: V1ObjectReference = Field(default_factory=lambda: V1ObjectReference())

    reporting_controller: str | None = Field(
        default=None,
        serialization_alias="reportingController",
        validation_alias=AliasChoices("reporting_controller", "reportingController"),
    )

    reporting_instance: str | None = Field(
        default=None,
        serialization_alias="reportingInstance",
        validation_alias=AliasChoices("reporting_instance", "reportingInstance"),
    )

    series: EventsV1EventSeries = Field(default_factory=lambda: EventsV1EventSeries())

    type: str | None = Field(default=None)
