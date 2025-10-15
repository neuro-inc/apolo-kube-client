from pydantic import BaseModel, Field

from .v1_label_selector import V1LabelSelector
from .v1_pod_template_spec import V1PodTemplateSpec


class V1ReplicaSetSpec(BaseModel):
    min_ready_seconds: int | None = Field(None, alias="minReadySeconds")

    replicas: int | None = Field(None, alias="replicas")

    selector: V1LabelSelector | None = Field(None, alias="selector")

    template: V1PodTemplateSpec | None = Field(None, alias="template")
