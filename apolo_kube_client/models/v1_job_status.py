from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_job_condition import V1JobCondition
from .v1_uncounted_terminated_pods import V1UncountedTerminatedPods
from datetime import datetime

__all__ = ("V1JobStatus",)


class V1JobStatus(BaseModel):
    active: int | None = Field(default=None)

    completed_indexes: str | None = Field(
        default=None,
        serialization_alias="completedIndexes",
        validation_alias=AliasChoices("completed_indexes", "completedIndexes"),
    )

    completion_time: datetime | None = Field(
        default=None,
        serialization_alias="completionTime",
        validation_alias=AliasChoices("completion_time", "completionTime"),
    )

    conditions: list[V1JobCondition] = Field(default=[])

    failed: int | None = Field(default=None)

    failed_indexes: str | None = Field(
        default=None,
        serialization_alias="failedIndexes",
        validation_alias=AliasChoices("failed_indexes", "failedIndexes"),
    )

    ready: int | None = Field(default=None)

    start_time: datetime | None = Field(
        default=None,
        serialization_alias="startTime",
        validation_alias=AliasChoices("start_time", "startTime"),
    )

    succeeded: int | None = Field(default=None)

    terminating: int | None = Field(default=None)

    uncounted_terminated_pods: V1UncountedTerminatedPods = Field(
        default_factory=lambda: V1UncountedTerminatedPods(),
        serialization_alias="uncountedTerminatedPods",
        validation_alias=AliasChoices(
            "uncounted_terminated_pods", "uncountedTerminatedPods"
        ),
    )
