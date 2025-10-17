from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_job_spec import V1JobSpec
from .v1_job_status import V1JobStatus
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1Job",)


class V1Job(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    spec: V1JobSpec = Field(default_factory=lambda: V1JobSpec())

    status: V1JobStatus = Field(default_factory=lambda: V1JobStatus())
