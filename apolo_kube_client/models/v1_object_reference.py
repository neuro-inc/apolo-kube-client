from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ObjectReference",)


class V1ObjectReference(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    field_path: str | None = Field(default_factory=lambda: None, alias="fieldPath")

    kind: str | None = Field(default_factory=lambda: None)

    name: str | None = Field(default_factory=lambda: None)

    namespace: str | None = Field(default_factory=lambda: None)

    resource_version: str | None = Field(
        default_factory=lambda: None, alias="resourceVersion"
    )

    uid: str | None = Field(default_factory=lambda: None)
