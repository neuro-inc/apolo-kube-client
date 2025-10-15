from pydantic import BaseModel, Field

from .v1_pod_template_spec import V1PodTemplateSpec


class V1ReplicationControllerSpec(BaseModel):
    min_ready_seconds: int | None = Field(None, alias="minReadySeconds")

    replicas: int | None = Field(None, alias="replicas")

    selector: dict(str, str) | None = Field(None, alias="selector")

    template: V1PodTemplateSpec | None = Field(None, alias="template")
