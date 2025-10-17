from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_job_condition import V1JobCondition
from .v1_uncounted_terminated_pods import V1UncountedTerminatedPods
from datetime import datetime

__all__ = ("V1JobStatus",)


class V1JobStatus(BaseModel):
    active: int | None = Field(default_factory=lambda: None)

    completed_indexes: str | None = Field(
        default_factory=lambda: None, alias="completedIndexes"
    )

    completion_time: datetime | None = Field(
        default_factory=lambda: None, alias="completionTime"
    )

    conditions: list[V1JobCondition] = Field(default_factory=lambda: [])

    failed: int | None = Field(default_factory=lambda: None)

    failed_indexes: str | None = Field(
        default_factory=lambda: None, alias="failedIndexes"
    )

    ready: int | None = Field(default_factory=lambda: None)

    start_time: datetime | None = Field(default_factory=lambda: None, alias="startTime")

    succeeded: int | None = Field(default_factory=lambda: None)

    terminating: int | None = Field(default_factory=lambda: None)

    uncounted_terminated_pods: V1UncountedTerminatedPods = Field(
        default_factory=lambda: V1UncountedTerminatedPods(),
        alias="uncountedTerminatedPods",
    )
