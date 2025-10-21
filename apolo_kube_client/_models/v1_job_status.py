from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1_job_condition import V1JobCondition
from .v1_uncounted_terminated_pods import V1UncountedTerminatedPods
from datetime import datetime
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1JobStatus",)


class V1JobStatus(BaseModel):
    active: int | None = None

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

    conditions: Annotated[
        list[V1JobCondition], BeforeValidator(_collection_if_none("[]"))
    ] = []

    failed: int | None = None

    failed_indexes: str | None = Field(
        default=None,
        serialization_alias="failedIndexes",
        validation_alias=AliasChoices("failed_indexes", "failedIndexes"),
    )

    ready: int | None = None

    start_time: datetime | None = Field(
        default=None,
        serialization_alias="startTime",
        validation_alias=AliasChoices("start_time", "startTime"),
    )

    succeeded: int | None = None

    terminating: int | None = None

    uncounted_terminated_pods: Annotated[
        V1UncountedTerminatedPods,
        BeforeValidator(_default_if_none(V1UncountedTerminatedPods)),
    ] = Field(
        default_factory=lambda: V1UncountedTerminatedPods(),
        serialization_alias="uncountedTerminatedPods",
        validation_alias=AliasChoices(
            "uncounted_terminated_pods", "uncountedTerminatedPods"
        ),
    )
