from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_object_meta import V1ObjectMeta
from apolo_kube_client._typedefs import JsonType

__all__ = ("V1ControllerRevision",)


class V1ControllerRevision(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    data: JsonType = Field(default={})

    kind: str | None = Field(default=None)

    metadata: V1ObjectMeta

    revision: int | None = Field(default=None)
