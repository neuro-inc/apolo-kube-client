from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_pod_spec import V1PodSpec
from .v1_pod_status import V1PodStatus

__all__ = ("V1Pod",)


class V1Pod(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    spec: V1PodSpec = Field(default_factory=lambda: V1PodSpec())

    status: V1PodStatus = Field(default_factory=lambda: V1PodStatus())
