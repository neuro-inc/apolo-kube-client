from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .v1_job_template_spec import V1JobTemplateSpec
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CronJobSpec",)


class V1CronJobSpec(BaseModel):
    concurrency_policy: str | None = Field(
        default=None,
        serialization_alias="concurrencyPolicy",
        validation_alias=AliasChoices("concurrency_policy", "concurrencyPolicy"),
    )

    failed_jobs_history_limit: int | None = Field(
        default=None,
        serialization_alias="failedJobsHistoryLimit",
        validation_alias=AliasChoices(
            "failed_jobs_history_limit", "failedJobsHistoryLimit"
        ),
    )

    job_template: Annotated[
        V1JobTemplateSpec, BeforeValidator(_default_if_none(V1JobTemplateSpec))
    ] = Field(
        default_factory=lambda: V1JobTemplateSpec(),
        serialization_alias="jobTemplate",
        validation_alias=AliasChoices("job_template", "jobTemplate"),
    )

    schedule: str | None = None

    starting_deadline_seconds: int | None = Field(
        default=None,
        serialization_alias="startingDeadlineSeconds",
        validation_alias=AliasChoices(
            "starting_deadline_seconds", "startingDeadlineSeconds"
        ),
    )

    successful_jobs_history_limit: int | None = Field(
        default=None,
        serialization_alias="successfulJobsHistoryLimit",
        validation_alias=AliasChoices(
            "successful_jobs_history_limit", "successfulJobsHistoryLimit"
        ),
    )

    suspend: bool | None = None

    time_zone: str | None = Field(
        default=None,
        serialization_alias="timeZone",
        validation_alias=AliasChoices("time_zone", "timeZone"),
    )
