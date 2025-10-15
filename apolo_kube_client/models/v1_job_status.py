from datetime import datetime

from pydantic import BaseModel, Field

from .v1_job_condition import V1JobCondition
from .v1_uncounted_terminated_pods import V1UncountedTerminatedPods


class V1JobStatus(BaseModel):
    active: int | None = Field(None, alias="active")

    completed_indexes: str | None = Field(None, alias="completedIndexes")

    completion_time: datetime | None = Field(None, alias="completionTime")

    conditions: list[V1JobCondition] | None = Field(None, alias="conditions")

    failed: int | None = Field(None, alias="failed")

    failed_indexes: str | None = Field(None, alias="failedIndexes")

    ready: int | None = Field(None, alias="ready")

    start_time: datetime | None = Field(None, alias="startTime")

    succeeded: int | None = Field(None, alias="succeeded")

    terminating: int | None = Field(None, alias="terminating")

    uncounted_terminated_pods: V1UncountedTerminatedPods | None = Field(
        None, alias="uncountedTerminatedPods"
    )
