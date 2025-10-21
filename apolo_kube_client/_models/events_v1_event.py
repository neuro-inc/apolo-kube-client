from pydantic import AliasChoices, Field
from .base import ResourceModel
from .events_v1_event_series import EventsV1EventSeries
from .utils import _default_if_none
from .v1_event_source import V1EventSource
from .v1_object_meta import V1ObjectMeta
from .v1_object_reference import V1ObjectReference
from datetime import datetime
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("EventsV1Event",)


class EventsV1Event(ResourceModel):
    action: str | None = None

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

    deprecated_source: Annotated[
        V1EventSource, BeforeValidator(_default_if_none(V1EventSource))
    ] = Field(
        default_factory=lambda: V1EventSource(),
        serialization_alias="deprecatedSource",
        validation_alias=AliasChoices("deprecated_source", "deprecatedSource"),
    )

    event_time: datetime | None = Field(
        default=None,
        serialization_alias="eventTime",
        validation_alias=AliasChoices("event_time", "eventTime"),
    )

    kind: str | None = None

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta())

    note: str | None = None

    reason: str | None = None

    regarding: Annotated[
        V1ObjectReference, BeforeValidator(_default_if_none(V1ObjectReference))
    ] = Field(default_factory=lambda: V1ObjectReference())

    related: Annotated[
        V1ObjectReference, BeforeValidator(_default_if_none(V1ObjectReference))
    ] = Field(default_factory=lambda: V1ObjectReference())

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

    series: Annotated[
        EventsV1EventSeries, BeforeValidator(_default_if_none(EventsV1EventSeries))
    ] = Field(default_factory=lambda: EventsV1EventSeries())

    type: str | None = None
