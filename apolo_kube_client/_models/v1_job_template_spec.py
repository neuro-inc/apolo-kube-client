from pydantic import Field
from .base import ResourceModel
from .v1_job_spec import V1JobSpec
from .v1_object_meta import V1ObjectMeta

__all__ = ("V1JobTemplateSpec",)


class V1JobTemplateSpec(ResourceModel):
    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1JobSpec = Field(default_factory=lambda: V1JobSpec())
