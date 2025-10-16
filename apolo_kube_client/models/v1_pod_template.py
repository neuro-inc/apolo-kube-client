from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_pod_template_spec import V1PodTemplateSpec

__all__ = ("V1PodTemplate",)


class V1PodTemplate(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    template: V1PodTemplateSpec = Field(
        default_factory=lambda: V1PodTemplateSpec(), alias="template"
    )
