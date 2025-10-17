from pydantic import AliasChoices, BaseModel, Field
from datetime import datetime

__all__ = ("EventsV1EventSeries",)


class EventsV1EventSeries(BaseModel):
    count: int | None = None

    last_observed_time: datetime | None = Field(
        default=None,
        serialization_alias="lastObservedTime",
        validation_alias=AliasChoices("last_observed_time", "lastObservedTime"),
    )
