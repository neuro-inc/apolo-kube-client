from __future__ import annotations
from pydantic import BaseModel, Field


__all__ = ("V1alpha1NamedRuleWithOperations",)


class V1alpha1NamedRuleWithOperations(BaseModel):
    api_groups: list[str] = Field(default_factory=lambda: [], alias="apiGroups")

    api_versions: list[str] = Field(default_factory=lambda: [], alias="apiVersions")

    operations: list[str] = Field(default_factory=lambda: [])

    resource_names: list[str] = Field(default_factory=lambda: [], alias="resourceNames")

    resources: list[str] = Field(default_factory=lambda: [])

    scope: str | None = Field(default_factory=lambda: None)
