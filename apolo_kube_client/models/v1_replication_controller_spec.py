from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_pod_template_spec import V1PodTemplateSpec

__all__ = ("V1ReplicationControllerSpec",)


class V1ReplicationControllerSpec(BaseModel):
    min_ready_seconds: int | None = Field(
        default_factory=lambda: None, alias="minReadySeconds"
    )

    replicas: int | None = Field(default_factory=lambda: None)

    selector: dict[str, str] = Field(default_factory=lambda: {})

    template: V1PodTemplateSpec = Field(default_factory=lambda: V1PodTemplateSpec())
