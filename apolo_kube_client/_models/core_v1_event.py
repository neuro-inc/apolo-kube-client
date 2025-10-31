from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ResourceModel
from .core_v1_event_series import CoreV1EventSeries
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_event_source import V1EventSource
from .v1_object_meta import V1ObjectMeta
from .v1_object_reference import V1ObjectReference
from datetime import datetime
from pydantic import BeforeValidator

__all__ = ("CoreV1Event",)


class CoreV1Event(ResourceModel):
    """Event is a report of an event somewhere in the cluster.  Events have a limited retention time and triggers and messages may evolve with time.  Event consumers should not rely on the timing of an event with a given Reason reflecting a consistent underlying trigger, or the continued existence of events with that Reason.  Events should be treated as informative, best-effort, supplemental data."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.Event"

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="", kind="Event", version="v1"
    )

    action: Annotated[
        str | None,
        Field(
            description="""What action was taken/failed regarding to the Regarding object.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "v1"

    count: Annotated[
        int | None,
        Field(
            description="""The number of times this event has occurred.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    event_time: Annotated[
        datetime | None,
        Field(
            alias="eventTime",
            description="""Time when this Event was first observed.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    first_timestamp: Annotated[
        datetime | None,
        Field(
            alias="firstTimestamp",
            description="""The time at which the event was first recorded. (Time of server receipt is in TypeMeta.)""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    involved_object: Annotated[
        V1ObjectReference,
        Field(
            alias="involvedObject",
            description="""The object that this event is about.""",
        ),
    ]

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "Event"

    last_timestamp: Annotated[
        datetime | None,
        Field(
            alias="lastTimestamp",
            description="""The time at which the most recent occurrence of this event was recorded.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    message: Annotated[
        str | None,
        Field(
            description="""A human-readable description of the status of this operation.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata"""
        ),
    ]

    reason: Annotated[
        str | None,
        Field(
            description="""This should be a short, machine understandable string that gives the reason for the transition into the object's current status.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    related: Annotated[
        V1ObjectReference,
        Field(
            description="""Optional secondary object for more complex actions.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectReference)),
    ] = V1ObjectReference()

    reporting_component: Annotated[
        str | None,
        Field(
            alias="reportingComponent",
            description="""Name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    reporting_instance: Annotated[
        str | None,
        Field(
            alias="reportingInstance",
            description="""ID of the controller instance, e.g. `kubelet-xyzf`.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    series: Annotated[
        CoreV1EventSeries,
        Field(
            description="""Data about the Event series this event represents or nil if it's a singleton Event.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(CoreV1EventSeries)),
    ] = CoreV1EventSeries()

    source: Annotated[
        V1EventSource,
        Field(
            description="""The component reporting this event. Should be a short machine understandable string.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1EventSource)),
    ] = V1EventSource()

    type: Annotated[
        str | None,
        Field(
            description="""Type of this event (Normal, Warning), new types could be added in the future""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
