from pydantic import BaseModel, Field

from .v1_object_meta import V1ObjectMeta


class V1PriorityClass(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    description: str | None = Field(None, alias="description")

    global_default: bool | None = Field(None, alias="globalDefault")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    preemption_policy: str | None = Field(None, alias="preemptionPolicy")

    value: int | None = Field(None, alias="value")
