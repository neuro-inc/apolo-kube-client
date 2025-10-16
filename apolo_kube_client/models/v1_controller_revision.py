from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1ControllerRevision",)


class V1ControllerRevision(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    data: JsonType = Field(default_factory=lambda: {}, alias="data")

    kind: str | None = Field(default_factory=lambda: None, alias="kind")

    metadata: V1ObjectMeta = Field(
        default_factory=lambda: V1ObjectMeta(), alias="metadata"
    )

    revision: int | None = Field(default_factory=lambda: None, alias="revision")
