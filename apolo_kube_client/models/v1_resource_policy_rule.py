from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1ResourcePolicyRule",)


class V1ResourcePolicyRule(BaseModel):
    api_groups: list[str] | None = Field(None, alias="apiGroups")

    cluster_scope: bool | None = Field(None, alias="clusterScope")

    namespaces: list[str] | None = Field(None, alias="namespaces")

    resources: list[str] | None = Field(None, alias="resources")

    verbs: list[str] | None = Field(None, alias="verbs")
