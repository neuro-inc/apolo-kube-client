from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_cron_job_spec import V1CronJobSpec
from .v1_cron_job_status import V1CronJobStatus
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1CronJob",)


class V1CronJob(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V1CronJobSpec = Field(default_factory=lambda: V1CronJobSpec(), alias="spec")

    status: V1CronJobStatus = Field(
        default_factory=lambda: V1CronJobStatus(), alias="status"
    )
