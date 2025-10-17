from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_pod_template_spec import V1PodTemplateSpec

__all__ = ("V1ReplicationControllerSpec",)


class V1ReplicationControllerSpec(BaseModel):
    min_ready_seconds: int | None = Field(
        default=None,
        serialization_alias="minReadySeconds",
        validation_alias=AliasChoices("min_ready_seconds", "minReadySeconds"),
    )

    replicas: int | None = Field(default=None)

    selector: dict[str, str] = Field(default={})

    template: V1PodTemplateSpec = Field(default_factory=lambda: V1PodTemplateSpec())
