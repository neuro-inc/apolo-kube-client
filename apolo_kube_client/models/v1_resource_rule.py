from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ResourceRule",)


class V1ResourceRule(BaseModel):
    api_groups: list[str] = Field(default_factory=lambda: [], alias="apiGroups")

    resource_names: list[str] = Field(default_factory=lambda: [], alias="resourceNames")

    resources: list[str] = Field(default_factory=lambda: [], alias="resources")

    verbs: list[str] = Field(default_factory=lambda: [], alias="verbs")
