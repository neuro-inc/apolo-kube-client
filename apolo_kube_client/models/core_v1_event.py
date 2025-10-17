from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .core_v1_event_series import CoreV1EventSeries
from .v1_event_source import V1EventSource
from .v1_object_meta import V1ObjectMeta
from .v1_object_reference import V1ObjectReference
from datetime import datetime

__all__ = ("CoreV1Event",)


class CoreV1Event(BaseModel):
    action: str | None = Field(default=None)

    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    count: int | None = Field(default=None)

    event_time: datetime | None = Field(
        default=None,
        serialization_alias="eventTime",
        validation_alias=AliasChoices("event_time", "eventTime"),
    )

    first_timestamp: datetime | None = Field(
        default=None,
        serialization_alias="firstTimestamp",
        validation_alias=AliasChoices("first_timestamp", "firstTimestamp"),
    )

    involved_object: V1ObjectReference = Field(
        default_factory=lambda: V1ObjectReference(),
        serialization_alias="involvedObject",
        validation_alias=AliasChoices("involved_object", "involvedObject"),
    )

    kind: str | None = Field(default=None)

    last_timestamp: datetime | None = Field(
        default=None,
        serialization_alias="lastTimestamp",
        validation_alias=AliasChoices("last_timestamp", "lastTimestamp"),
    )

    message: str | None = Field(default=None)

    metadata: V1ObjectMeta

    reason: str | None = Field(default=None)

    related: V1ObjectReference = Field(default_factory=lambda: V1ObjectReference())

    reporting_component: str | None = Field(
        default=None,
        serialization_alias="reportingComponent",
        validation_alias=AliasChoices("reporting_component", "reportingComponent"),
    )

    reporting_instance: str | None = Field(
        default=None,
        serialization_alias="reportingInstance",
        validation_alias=AliasChoices("reporting_instance", "reportingInstance"),
    )

    series: CoreV1EventSeries = Field(default_factory=lambda: CoreV1EventSeries())

    source: V1EventSource = Field(default_factory=lambda: V1EventSource())

    type: str | None = Field(default=None)
