from pydantic import Field
from .base import ResourceModel
from .v1_object_meta import V1ObjectMeta
from .v1_pod_spec import V1PodSpec

__all__ = ("V1PodTemplateSpec",)


class V1PodTemplateSpec(ResourceModel):
    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1PodSpec = Field(default_factory=lambda: V1PodSpec())
