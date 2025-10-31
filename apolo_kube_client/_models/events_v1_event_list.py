from typing import Annotated, ClassVar, Final
from pydantic import ConfigDict, Field
from .base import ListModel
from .events_v1_event import EventsV1Event
from .utils import KubeMeta
from .utils import _default_if_none
from .v1_list_meta import V1ListMeta
from pydantic import BeforeValidator

__all__ = ("EventsV1EventList",)


class EventsV1EventList(ListModel):
    """EventList is a list of Event objects."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.events.v1.EventList"

    kubernetes_meta: ClassVar[Final[tuple[KubeMeta, ...]]] = KubeMeta(
        group="events.k8s.io", kind="EventList", version="v1"
    )

    api_version: Annotated[
        str,
        Field(
            alias="apiVersion",
            description="""APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources""",
        ),
    ] = "events.k8s.io/v1"

    items: Annotated[
        list[EventsV1Event], Field(description="""items is a list of schema objects.""")
    ]

    kind: Annotated[
        str,
        Field(
            description="""Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds"""
        ),
    ] = "EventList"

    metadata: Annotated[
        V1ListMeta,
        Field(
            description="""Standard list metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata""",
            exclude_if=lambda v: not v.__pydantic_fields_set__,
        ),
        BeforeValidator(_default_if_none(V1ListMeta)),
    ] = V1ListMeta()
