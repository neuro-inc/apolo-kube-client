from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta
from .v1_pod_template_spec import V1PodTemplateSpec

__all__ = ("V1PodTemplate",)


class V1PodTemplate(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    template: V1PodTemplateSpec | None = Field(None, alias="template")
