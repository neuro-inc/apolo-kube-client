from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_job_condition import V1JobCondition
from .v1_uncounted_terminated_pods import V1UncountedTerminatedPods
from datetime import datetime
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1JobStatus",)


class V1JobStatus(BaseModel):
    active: int | None = Field(default=None, exclude_if=_exclude_if)

    completed_indexes: str | None = Field(
        default=None,
        serialization_alias="completedIndexes",
        validation_alias=AliasChoices("completed_indexes", "completedIndexes"),
        exclude_if=_exclude_if,
    )

    completion_time: datetime | None = Field(
        default=None,
        serialization_alias="completionTime",
        validation_alias=AliasChoices("completion_time", "completionTime"),
        exclude_if=_exclude_if,
    )

    conditions: Annotated[
        list[V1JobCondition], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)

    failed: int | None = Field(default=None, exclude_if=_exclude_if)

    failed_indexes: str | None = Field(
        default=None,
        serialization_alias="failedIndexes",
        validation_alias=AliasChoices("failed_indexes", "failedIndexes"),
        exclude_if=_exclude_if,
    )

    ready: int | None = Field(default=None, exclude_if=_exclude_if)

    start_time: datetime | None = Field(
        default=None,
        serialization_alias="startTime",
        validation_alias=AliasChoices("start_time", "startTime"),
        exclude_if=_exclude_if,
    )

    succeeded: int | None = Field(default=None, exclude_if=_exclude_if)

    terminating: int | None = Field(default=None, exclude_if=_exclude_if)

    uncounted_terminated_pods: Annotated[
        V1UncountedTerminatedPods,
        BeforeValidator(_default_if_none(V1UncountedTerminatedPods)),
    ] = Field(
        default_factory=lambda: V1UncountedTerminatedPods(),
        serialization_alias="uncountedTerminatedPods",
        validation_alias=AliasChoices(
            "uncounted_terminated_pods", "uncountedTerminatedPods"
        ),
        exclude_if=_exclude_if,
    )
