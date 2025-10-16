from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = ("V1RuleWithOperations",)


class V1RuleWithOperations(BaseModel):
    api_groups: list[str] | None = Field(None, alias="apiGroups")

    api_versions: list[str] | None = Field(None, alias="apiVersions")

    operations: list[str] | None = Field(None, alias="operations")

    resources: list[str] | None = Field(None, alias="resources")

    scope: str | None = Field(None, alias="scope")
