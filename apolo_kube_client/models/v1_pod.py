from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from .v1_pod_spec import V1PodSpec
from .v1_pod_status import V1PodStatus

__all__ = ("V1Pod",)


class V1Pod(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    kind: str | None = Field(default_factory=lambda: None)

    metadata: V1ObjectMeta = Field(default_factory=lambda: V1ObjectMeta())

    spec: V1PodSpec = Field(default_factory=lambda: V1PodSpec())

    status: V1PodStatus = Field(default_factory=lambda: V1PodStatus())
