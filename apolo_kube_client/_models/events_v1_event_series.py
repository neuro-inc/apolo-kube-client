from pydantic import AliasChoices, BaseModel, Field
from .utils import _exclude_if
from datetime import datetime

__all__ = ("EventsV1EventSeries",)


class EventsV1EventSeries(BaseModel):
    count: int | None = Field(default=None, exclude_if=_exclude_if)

    last_observed_time: datetime | None = Field(
        default=None,
        serialization_alias="lastObservedTime",
        validation_alias=AliasChoices("last_observed_time", "lastObservedTime"),
        exclude_if=_exclude_if,
    )
