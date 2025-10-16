from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1ObjectReference",)


class V1ObjectReference(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    field_path: str | None = Field(None, alias="fieldPath")

    kind: str | None = Field(None, alias="kind")

    name: str | None = Field(None, alias="name")

    namespace: str | None = Field(None, alias="namespace")

    resource_version: str | None = Field(None, alias="resourceVersion")

    uid: str | None = Field(None, alias="uid")
