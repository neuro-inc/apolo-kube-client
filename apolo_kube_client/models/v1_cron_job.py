from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_cron_job_spec import V1CronJobSpec
from .v1_cron_job_status import V1CronJobStatus
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1CronJob",)


class V1CronJob(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1CronJobSpec | None = Field(None, alias="spec")

    status: V1CronJobStatus | None = Field(None, alias="status")
