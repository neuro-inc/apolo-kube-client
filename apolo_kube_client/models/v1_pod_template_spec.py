from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_pod_spec import V1PodSpec

__all__ = ("V1PodTemplateSpec",)


class V1PodTemplateSpec(BaseModel):
    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    spec: V1PodSpec = Field(default_factory=lambda: V1PodSpec(), alias="spec")
