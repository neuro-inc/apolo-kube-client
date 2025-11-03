from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ResourceModel
from .events_v1_event_series import EventsV1EventSeries
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_event_source import V1EventSource
from .v1_object_meta import V1ObjectMeta
from .v1_object_reference import V1ObjectReference
from datetime import datetime
from pydantic import BeforeValidator

__all__ = ("EventsV1Event",)


class EventsV1Event(ResourceModel):
    """Event is a report of an event somewhere in the cluster. It generally denotes some state change in the system. Events have a limited retention time and triggers and messages may evolve with time.  Event consumers should not rely on the timing of an event with a given Reason reflecting a consistent underlying trigger, or the continued existence of events with that Reason.  Events should be treated as informative, best-effort, supplemental data."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.events.v1.Event"

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="events.k8s.io", kind="Event", version="v1"
    )

    action: Annotated[
        str | None,
        Field(
            description="""action is what action was taken/failed regarding to the regarding object. It is machine-readable. This field cannot be empty for new Events and it can have at most 128 characters.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "events.k8s.io/v1"

    deprecated_count: Annotated[
        int | None,
        Field(
            alias="deprecatedCount",
            description="""deprecatedCount is the deprecated field assuring backward compatibility with core.v1 Event type.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    deprecated_first_timestamp: Annotated[
        datetime | None,
        Field(
            alias="deprecatedFirstTimestamp",
            description="""deprecatedFirstTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    deprecated_last_timestamp: Annotated[
        datetime | None,
        Field(
            alias="deprecatedLastTimestamp",
            description="""deprecatedLastTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    deprecated_source: Annotated[
        V1EventSource,
        Field(
            alias="deprecatedSource",
            description="""deprecatedSource is the deprecated field assuring backward compatibility with core.v1 Event type.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1EventSource)),
    ] = V1EventSource()

    event_time: Annotated[
        datetime,
        Field(
            alias="eventTime",
            description="""eventTime is the time when this Event was first observed. It is required.""",
        ),
    ]

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "Event"

    metadata: Annotated[
        V1ObjectMeta,
        Field(
            description="""Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectMeta)),
    ] = V1ObjectMeta()

    note: Annotated[
        str | None,
        Field(
            description="""note is a human-readable description of the status of this operation. Maximal length of the note is 1kB, but libraries should be prepared to handle values up to 64kB.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    reason: Annotated[
        str | None,
        Field(
            description="""reason is why the action was taken. It is human-readable. This field cannot be empty for new Events and it can have at most 128 characters.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    regarding: Annotated[
        V1ObjectReference,
        Field(
            description="""regarding contains the object this Event is about. In most cases it's an Object reporting controller implements, e.g. ReplicaSetController implements ReplicaSets and this event is emitted because it acts on some changes in a ReplicaSet object.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectReference)),
    ] = V1ObjectReference()

    related: Annotated[
        V1ObjectReference,
        Field(
            description="""related is the optional secondary object for more complex actions. E.g. when regarding object triggers a creation or deletion of related object.""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ObjectReference)),
    ] = V1ObjectReference()

    reporting_controller: Annotated[
        str | None,
        Field(
            alias="reportingController",
            description="""reportingController is the name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`. This field cannot be empty for new Events.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    reporting_instance: Annotated[
        str | None,
        Field(
            alias="reportingInstance",
            description="""reportingInstance is the ID of the controller instance, e.g. `kubelet-xyzf`. This field cannot be empty for new Events and it can have at most 128 characters.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    series: Annotated[
        EventsV1EventSeries | None,
        Field(
            description="""series is data about the Event series this event represents or nil if it's a singleton Event.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    type: Annotated[
        str | None,
        Field(
            description="""type is the type of this event (Normal, Warning), new types could be added in the future. It is machine-readable. This field cannot be empty for new Events.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
