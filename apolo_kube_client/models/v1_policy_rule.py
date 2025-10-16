from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1PolicyRule",)


class V1PolicyRule(BaseModel):
    api_groups: list[str] = Field(default_factory=lambda: [], alias="apiGroups")

    non_resource_ur_ls: list[str] = Field(
        default_factory=lambda: [], alias="nonResourceURLs"
    )

    resource_names: list[str] = Field(default_factory=lambda: [], alias="resourceNames")

    resources: list[str] = Field(default_factory=lambda: [], alias="resources")

    verbs: list[str] = Field(default_factory=lambda: [], alias="verbs")
