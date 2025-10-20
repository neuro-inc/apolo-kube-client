from pydantic import AliasChoices, Field
from .base import ResourceModel
from .core_v1_event_series import CoreV1EventSeries
from .v1_event_source import V1EventSource
from .v1_object_meta import V1ObjectMeta
from .v1_object_reference import V1ObjectReference
from datetime import datetime

__all__ = ("CoreV1Event",)


class CoreV1Event(ResourceModel):
    action: str | None = None

    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    count: int | None = None

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

    kind: str | None = None

    last_timestamp: datetime | None = Field(
        default=None,
        serialization_alias="lastTimestamp",
        validation_alias=AliasChoices("last_timestamp", "lastTimestamp"),
    )

    message: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    reason: str | None = None

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

    type: str | None = None
