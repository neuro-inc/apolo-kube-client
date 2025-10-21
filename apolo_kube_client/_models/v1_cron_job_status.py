from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1_object_reference import V1ObjectReference
from datetime import datetime
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CronJobStatus",)


class V1CronJobStatus(BaseModel):
    active: Annotated[
        list[V1ObjectReference], BeforeValidator(_collection_if_none("[]"))
    ] = []

    last_schedule_time: datetime | None = Field(
        default=None,
        serialization_alias="lastScheduleTime",
        validation_alias=AliasChoices("last_schedule_time", "lastScheduleTime"),
    )

    last_successful_time: datetime | None = Field(
        default=None,
        serialization_alias="lastSuccessfulTime",
        validation_alias=AliasChoices("last_successful_time", "lastSuccessfulTime"),
    )
