from __future__ import annotations

from pydantic import BaseModel, Field

from apolo_kube_client._typedefs import JsonType

from .v1_object_meta import V1ObjectMeta

__all__ = ("V1ControllerRevision",)


class V1ControllerRevision(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    data: JsonType | None = Field(None, alias="data")

    kind: str | None = Field(None, alias="kind")

    metadata: V1ObjectMeta | None = Field(None, alias="metadata")

    revision: int | None = Field(None, alias="revision")
