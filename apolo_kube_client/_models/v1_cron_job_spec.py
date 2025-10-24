from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1_job_template_spec import V1JobTemplateSpec

__all__ = ("V1CronJobSpec",)


class V1CronJobSpec(BaseModel):
    """CronJobSpec describes how the job execution will look like and when it will actually run."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.batch.v1.CronJobSpec"

    concurrency_policy: Annotated[
        str | None,
        Field(
            alias="concurrencyPolicy",
            description="""Specifies how to treat concurrent executions of a Job. Valid values are:

- "Allow" (default): allows CronJobs to run concurrently; - "Forbid": forbids concurrent runs, skipping next run if previous run hasn't finished yet; - "Replace": cancels currently running job and replaces it with a new one""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    failed_jobs_history_limit: Annotated[
        int | None,
        Field(
            alias="failedJobsHistoryLimit",
            description="""The number of failed finished jobs to retain. Value must be non-negative integer. Defaults to 1.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    job_template: Annotated[
        V1JobTemplateSpec,
        Field(
            alias="jobTemplate",
            description="""Specifies the job that will be created when executing a CronJob.""",
        ),
    ]

    schedule: Annotated[
        str,
        Field(
            description="""The schedule in Cron format, see https://en.wikipedia.org/wiki/Cron."""
        ),
    ]

    starting_deadline_seconds: Annotated[
        int | None,
        Field(
            alias="startingDeadlineSeconds",
            description="""Optional deadline in seconds for starting the job if it misses scheduled time for any reason.  Missed jobs executions will be counted as failed ones.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    successful_jobs_history_limit: Annotated[
        int | None,
        Field(
            alias="successfulJobsHistoryLimit",
            description="""The number of successful finished jobs to retain. Value must be non-negative integer. Defaults to 3.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    suspend: Annotated[
        bool | None,
        Field(
            description="""This flag tells the controller to suspend subsequent executions, it does not apply to already started executions.  Defaults to false.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    time_zone: Annotated[
        str | None,
        Field(
            alias="timeZone",
            description="""The time zone name for the given schedule, see https://en.wikipedia.org/wiki/List_of_tz_database_time_zones. If not specified, this will default to the time zone of the kube-controller-manager process. The set of valid time zone names and the time zone offset is loaded from the system-wide time zone database by the API server during CronJob validation and the controller manager during execution. If no system-wide time zone database can be found a bundled version of the database is used instead. If the time zone name becomes invalid during the lifetime of a CronJob or due to a change in host configuration, the controller will stop creating new new Jobs and will create a system event with the reason UnknownTimeZone. More information can be found in https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#time-zones""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
