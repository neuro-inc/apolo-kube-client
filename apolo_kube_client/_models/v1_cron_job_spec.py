from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_job_template_spec import V1JobTemplateSpec
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CronJobSpec",)


class V1CronJobSpec(BaseModel):
    concurrency_policy: str | None = Field(
        default=None,
        serialization_alias="concurrencyPolicy",
        validation_alias=AliasChoices("concurrency_policy", "concurrencyPolicy"),
        exclude_if=_exclude_if,
    )

    failed_jobs_history_limit: int | None = Field(
        default=None,
        serialization_alias="failedJobsHistoryLimit",
        validation_alias=AliasChoices(
            "failed_jobs_history_limit", "failedJobsHistoryLimit"
        ),
        exclude_if=_exclude_if,
    )

    job_template: Annotated[
        V1JobTemplateSpec, BeforeValidator(_default_if_none(V1JobTemplateSpec))
    ] = Field(
        default_factory=lambda: V1JobTemplateSpec(),
        serialization_alias="jobTemplate",
        validation_alias=AliasChoices("job_template", "jobTemplate"),
        exclude_if=_exclude_if,
    )

    schedule: str | None = Field(default=None, exclude_if=_exclude_if)

    starting_deadline_seconds: int | None = Field(
        default=None,
        serialization_alias="startingDeadlineSeconds",
        validation_alias=AliasChoices(
            "starting_deadline_seconds", "startingDeadlineSeconds"
        ),
        exclude_if=_exclude_if,
    )

    successful_jobs_history_limit: int | None = Field(
        default=None,
        serialization_alias="successfulJobsHistoryLimit",
        validation_alias=AliasChoices(
            "successful_jobs_history_limit", "successfulJobsHistoryLimit"
        ),
        exclude_if=_exclude_if,
    )

    suspend: bool | None = Field(default=None, exclude_if=_exclude_if)

    time_zone: str | None = Field(
        default=None,
        serialization_alias="timeZone",
        validation_alias=AliasChoices("time_zone", "timeZone"),
        exclude_if=_exclude_if,
    )
