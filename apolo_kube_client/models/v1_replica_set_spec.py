from pydantic import AliasChoices, BaseModel, Field
from .v1_label_selector import V1LabelSelector
from .v1_pod_template_spec import V1PodTemplateSpec

__all__ = ("V1ReplicaSetSpec",)


class V1ReplicaSetSpec(BaseModel):
    min_ready_seconds: int | None = Field(
        default=None,
        serialization_alias="minReadySeconds",
        validation_alias=AliasChoices("min_ready_seconds", "minReadySeconds"),
    )

    replicas: int | None = None

    selector: V1LabelSelector = Field(default_factory=lambda: V1LabelSelector())

    template: V1PodTemplateSpec = Field(default_factory=lambda: V1PodTemplateSpec())
