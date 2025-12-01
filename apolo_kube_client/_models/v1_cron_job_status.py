from datetime import datetime
from typing import Annotated, ClassVar, Final

from pydantic import BaseModel, BeforeValidator, Field

from .utils import _collection_if_none
from .v1_object_reference import V1ObjectReference


__all__ = ("V1CronJobStatus",)


class V1CronJobStatus(BaseModel):
    """CronJobStatus represents the current state of a cron job."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.batch.v1.CronJobStatus"

    active: Annotated[
        list[V1ObjectReference],
        Field(
            description="""A list of pointers to currently running jobs.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []

    last_schedule_time: Annotated[
        datetime | None,
        Field(
            alias="lastScheduleTime",
            description="""Information when was the last time the job was successfully scheduled.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    last_successful_time: Annotated[
        datetime | None,
        Field(
            alias="lastSuccessfulTime",
            description="""Information when was the last time the job successfully completed.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
