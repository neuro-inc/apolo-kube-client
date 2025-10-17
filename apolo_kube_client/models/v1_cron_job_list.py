from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_cron_job import V1CronJob
from .v1_list_meta import V1ListMeta

__all__ = ("V1CronJobList",)


class V1CronJobList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    items: list[V1CronJob] = Field(default_factory=lambda: [])

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ListMeta = Field(default_factory=lambda: V1ListMeta())
