from __future__ import annotations

from pydantic import BaseModel, Field

from .v1_api_group import V1APIGroup

__all__ = ("V1APIGroupList",)


class V1APIGroupList(BaseModel):
    api_version: str | None = Field(None, alias="apiVersion")

    groups: list[V1APIGroup] | None = Field(None, alias="groups")

    kind: str | None = Field(None, alias="kind")
