from pydantic import AliasChoices, Field
from .base import ResourceModel
from .events_v1_event_series import EventsV1EventSeries
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_event_source import V1EventSource
from .v1_object_meta import V1ObjectMeta
from .v1_object_reference import V1ObjectReference
from datetime import datetime
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("EventsV1Event",)


class EventsV1Event(ResourceModel):
    action: str | None = Field(default=None, exclude_if=_exclude_if)

    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
        exclude_if=_exclude_if,
    )

    deprecated_count: int | None = Field(
        default=None,
        serialization_alias="deprecatedCount",
        validation_alias=AliasChoices("deprecated_count", "deprecatedCount"),
        exclude_if=_exclude_if,
    )

    deprecated_first_timestamp: datetime | None = Field(
        default=None,
        serialization_alias="deprecatedFirstTimestamp",
        validation_alias=AliasChoices(
            "deprecated_first_timestamp", "deprecatedFirstTimestamp"
        ),
        exclude_if=_exclude_if,
    )

    deprecated_last_timestamp: datetime | None = Field(
        default=None,
        serialization_alias="deprecatedLastTimestamp",
        validation_alias=AliasChoices(
            "deprecated_last_timestamp", "deprecatedLastTimestamp"
        ),
        exclude_if=_exclude_if,
    )

    deprecated_source: Annotated[
        V1EventSource, BeforeValidator(_default_if_none(V1EventSource))
    ] = Field(
        default_factory=lambda: V1EventSource(),
        serialization_alias="deprecatedSource",
        validation_alias=AliasChoices("deprecated_source", "deprecatedSource"),
        exclude_if=_exclude_if,
    )

    event_time: datetime | None = Field(
        default=None,
        serialization_alias="eventTime",
        validation_alias=AliasChoices("event_time", "eventTime"),
        exclude_if=_exclude_if,
    )

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta(), exclude_if=_exclude_if)

    note: str | None = Field(default=None, exclude_if=_exclude_if)

    reason: str | None = Field(default=None, exclude_if=_exclude_if)

    regarding: Annotated[
        V1ObjectReference, BeforeValidator(_default_if_none(V1ObjectReference))
    ] = Field(default_factory=lambda: V1ObjectReference(), exclude_if=_exclude_if)

    related: Annotated[
        V1ObjectReference, BeforeValidator(_default_if_none(V1ObjectReference))
    ] = Field(default_factory=lambda: V1ObjectReference(), exclude_if=_exclude_if)

    reporting_controller: str | None = Field(
        default=None,
        serialization_alias="reportingController",
        validation_alias=AliasChoices("reporting_controller", "reportingController"),
        exclude_if=_exclude_if,
    )

    reporting_instance: str | None = Field(
        default=None,
        serialization_alias="reportingInstance",
        validation_alias=AliasChoices("reporting_instance", "reportingInstance"),
        exclude_if=_exclude_if,
    )

    series: Annotated[
        EventsV1EventSeries, BeforeValidator(_default_if_none(EventsV1EventSeries))
    ] = Field(default_factory=lambda: EventsV1EventSeries(), exclude_if=_exclude_if)

    type: str | None = Field(default=None, exclude_if=_exclude_if)
