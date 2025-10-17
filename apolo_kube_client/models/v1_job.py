from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_job_spec import V1JobSpec
from .v1_job_status import V1JobStatus
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1Job",)


class V1Job(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1JobSpec = Field(default_factory=lambda: V1JobSpec())

    status: V1JobStatus = Field(default_factory=lambda: V1JobStatus())
