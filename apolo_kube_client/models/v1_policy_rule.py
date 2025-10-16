from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1PolicyRule",)


class V1PolicyRule(BaseModel):
    api_groups: list[str] | None = Field(None, alias="apiGroups")

    non_resource_ur_ls: list[str] | None = Field(None, alias="nonResourceURLs")

    resource_names: list[str] | None = Field(None, alias="resourceNames")

    resources: list[str] | None = Field(None, alias="resources")

    verbs: list[str] | None = Field(None, alias="verbs")
