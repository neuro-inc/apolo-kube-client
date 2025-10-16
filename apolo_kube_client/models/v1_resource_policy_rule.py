from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1ResourcePolicyRule",)


class V1ResourcePolicyRule(BaseModel):
    api_groups: list[str] = Field(default_factory=lambda: [], alias="apiGroups")

    cluster_scope: bool | None = Field(
        default_factory=lambda: None, alias="clusterScope"
    )

    namespaces: list[str] = Field(default_factory=lambda: [], alias="namespaces")

    resources: list[str] = Field(default_factory=lambda: [], alias="resources")

    verbs: list[str] = Field(default_factory=lambda: [], alias="verbs")
