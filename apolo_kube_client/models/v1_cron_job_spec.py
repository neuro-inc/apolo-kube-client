from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_job_template_spec import V1JobTemplateSpec

__all__ = ("V1CronJobSpec",)


class V1CronJobSpec(BaseModel):
    concurrency_policy: str | None = Field(None, alias="concurrencyPolicy")

    failed_jobs_history_limit: int | None = Field(None, alias="failedJobsHistoryLimit")

    job_template: V1JobTemplateSpec | None = Field(None, alias="jobTemplate")

    schedule: str | None = Field(None, alias="schedule")

    starting_deadline_seconds: int | None = Field(None, alias="startingDeadlineSeconds")

    successful_jobs_history_limit: int | None = Field(
        None, alias="successfulJobsHistoryLimit"
    )

    suspend: bool | None = Field(None, alias="suspend")

    time_zone: str | None = Field(None, alias="timeZone")
