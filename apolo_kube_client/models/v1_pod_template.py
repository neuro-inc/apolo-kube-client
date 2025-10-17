from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_pod_template_spec import V1PodTemplateSpec

__all__ = ("V1PodTemplate",)


class V1PodTemplate(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    template: V1PodTemplateSpec = Field(default_factory=lambda: V1PodTemplateSpec())
