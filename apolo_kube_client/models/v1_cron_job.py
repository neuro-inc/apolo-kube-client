from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_cron_job_spec import V1CronJobSpec
from .v1_cron_job_status import V1CronJobStatus
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1CronJob",)


class V1CronJob(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    spec: V1CronJobSpec = Field(default_factory=lambda: V1CronJobSpec())

    status: V1CronJobStatus = Field(default_factory=lambda: V1CronJobStatus())
