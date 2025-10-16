from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_job_spec import V1JobSpec
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1JobTemplateSpec",)


class V1JobTemplateSpec(BaseModel):
    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    spec: V1JobSpec | None = Field(None, alias="spec")
