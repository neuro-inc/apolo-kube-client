from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_job_spec import V1JobSpec
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1JobTemplateSpec",)


class V1JobTemplateSpec(BaseModel):
    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1JobSpec = Field(default_factory=lambda: V1JobSpec())
