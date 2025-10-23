from pydantic import AliasChoices, Field
from .base import ResourceModel
from .core_v1_event_series import CoreV1EventSeries
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_event_source import V1EventSource
from .v1_object_meta import V1ObjectMeta
from .v1_object_reference import V1ObjectReference
from datetime import datetime
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("CoreV1Event",)


class CoreV1Event(ResourceModel):
    action: str | None = Field(default=None, exclude_if=_exclude_if)

    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
        exclude_if=_exclude_if,
    )

    count: int | None = Field(default=None, exclude_if=_exclude_if)

    event_time: datetime | None = Field(
        default=None,
        serialization_alias="eventTime",
        validation_alias=AliasChoices("event_time", "eventTime"),
        exclude_if=_exclude_if,
    )

    first_timestamp: datetime | None = Field(
        default=None,
        serialization_alias="firstTimestamp",
        validation_alias=AliasChoices("first_timestamp", "firstTimestamp"),
        exclude_if=_exclude_if,
    )

    involved_object: Annotated[
        V1ObjectReference, BeforeValidator(_default_if_none(V1ObjectReference))
    ] = Field(
        default_factory=lambda: V1ObjectReference(),
        serialization_alias="involvedObject",
        validation_alias=AliasChoices("involved_object", "involvedObject"),
        exclude_if=_exclude_if,
    )

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    last_timestamp: datetime | None = Field(
        default=None,
        serialization_alias="lastTimestamp",
        validation_alias=AliasChoices("last_timestamp", "lastTimestamp"),
        exclude_if=_exclude_if,
    )

    message: str | None = Field(default=None, exclude_if=_exclude_if)

    metadata: Annotated[
        V1ObjectMeta, BeforeValidator(_default_if_none(V1ObjectMeta))
    ] = Field(default_factory=lambda: V1ObjectMeta(), exclude_if=_exclude_if)

    reason: str | None = Field(default=None, exclude_if=_exclude_if)

    related: Annotated[
        V1ObjectReference, BeforeValidator(_default_if_none(V1ObjectReference))
    ] = Field(default_factory=lambda: V1ObjectReference(), exclude_if=_exclude_if)

    reporting_component: str | None = Field(
        default=None,
        serialization_alias="reportingComponent",
        validation_alias=AliasChoices("reporting_component", "reportingComponent"),
        exclude_if=_exclude_if,
    )

    reporting_instance: str | None = Field(
        default=None,
        serialization_alias="reportingInstance",
        validation_alias=AliasChoices("reporting_instance", "reportingInstance"),
        exclude_if=_exclude_if,
    )

    series: Annotated[
        CoreV1EventSeries, BeforeValidator(_default_if_none(CoreV1EventSeries))
    ] = Field(default_factory=lambda: CoreV1EventSeries(), exclude_if=_exclude_if)

    source: Annotated[
        V1EventSource, BeforeValidator(_default_if_none(V1EventSource))
    ] = Field(default_factory=lambda: V1EventSource(), exclude_if=_exclude_if)

    type: str | None = Field(default=None, exclude_if=_exclude_if)
