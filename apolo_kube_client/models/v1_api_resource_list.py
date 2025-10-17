from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_api_resource import V1APIResource

__all__ = ("V1APIResourceList",)


class V1APIResourceList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    group_version: str | None = Field(
        default_factory=lambda: None, alias="groupVersion"
    )

    kind: str | None = Field(default_factory=lambda: None)

    resources: list[V1APIResource] = Field(default_factory=lambda: [])
