from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_api_resource import V1APIResource

__all__ = ("V1APIResourceList",)


class V1APIResourceList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    group_version: str | None = Field(None, alias="groupVersion")

    kind: str | None = Field(None, alias="kind")

    resources: list[V1APIResource] | None = Field(None, alias="resources")
