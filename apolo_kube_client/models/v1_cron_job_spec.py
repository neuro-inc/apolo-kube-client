from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_job_template_spec import V1JobTemplateSpec

__all__ = ("V1CronJobSpec",)


class V1CronJobSpec(BaseModel):
    concurrency_policy: str | None = Field(
        default_factory=lambda: None, alias="concurrencyPolicy"
    )

    failed_jobs_history_limit: int | None = Field(
        default_factory=lambda: None, alias="failedJobsHistoryLimit"
    )

    job_template: V1JobTemplateSpec = Field(
        default_factory=lambda: V1JobTemplateSpec(), alias="jobTemplate"
    )

    schedule: str | None = Field(default_factory=lambda: None)

    starting_deadline_seconds: int | None = Field(
        default_factory=lambda: None, alias="startingDeadlineSeconds"
    )

    successful_jobs_history_limit: int | None = Field(
        default_factory=lambda: None, alias="successfulJobsHistoryLimit"
    )

    suspend: bool | None = Field(default_factory=lambda: None)

    time_zone: str | None = Field(default_factory=lambda: None, alias="timeZone")
