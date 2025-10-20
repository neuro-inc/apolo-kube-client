from pydantic import AliasChoices, Field
from .base import ResourceModel
from .v1_job_spec import V1JobSpec
from .v1_job_status import V1JobStatus
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1Job",)


class V1Job(ResourceModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = None

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1JobSpec = Field(default_factory=lambda: V1JobSpec())

    status: V1JobStatus = Field(default_factory=lambda: V1JobStatus())
