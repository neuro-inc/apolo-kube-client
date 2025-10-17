from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_cron_job import V1CronJob
from .v1_list_meta import V1ListMeta

__all__ = ("V1CronJobList",)


class V1CronJobList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    items: list[V1CronJob] = Field(default=[])

    kind: str | None = Field(default=None)

    metadata: V1ListMeta
