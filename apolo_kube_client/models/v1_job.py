from pydantic import BaseModel, Field

from .v1_job_spec import V1JobSpec
from .v1_job_status import V1JobStatus
from .v1_object_meta import V1ObjectMeta


class V1Job(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1JobSpec | None = Field(None, alias="spec")

    status: V1JobStatus | None = Field(None, alias="status")
