from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

__all__ = ("EventsV1EventSeries",)


class EventsV1EventSeries(BaseModel):
    """EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time. How often to update the EventSeries is up to the event reporters. The default event reporter in "k8s.io/client-go/tools/events/event_broadcaster.go" shows how this struct is updated on heartbeats and can guide customized reporter implementations."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.events.v1.EventSeries"

    count: Annotated[
        int,
        Field(
            description="""count is the number of occurrences in this series up to the last heartbeat time."""
        ),
    ]

    last_observed_time: Annotated[
        datetime,
        Field(
            alias="lastObservedTime",
            description="""lastObservedTime is the time when last Event from the series was seen before last heartbeat.""",
        ),
    ]
