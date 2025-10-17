from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_api_group import V1APIGroup

__all__ = ("V1APIGroupList",)


class V1APIGroupList(BaseModel):
    api_version: str | None = Field(default_factory=lambda: None, alias="apiVersion")

    groups: list[V1APIGroup] = Field(default_factory=lambda: [])

    kind: str | None = Field(default_factory=lambda: None)
