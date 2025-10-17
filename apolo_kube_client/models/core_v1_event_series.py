from pydantic import AliasChoices, BaseModel, Field
from datetime import datetime

__all__ = ("CoreV1EventSeries",)


class CoreV1EventSeries(BaseModel):
    count: int | None = None

    last_observed_time: datetime | None = Field(
        default=None,
        serialization_alias="lastObservedTime",
        validation_alias=AliasChoices("last_observed_time", "lastObservedTime"),
    )
