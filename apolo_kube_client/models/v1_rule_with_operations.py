from pydantic import BaseModel, Field


class V1RuleWithOperations(BaseModel):
    api_groups: list[str] | None = Field(None, alias="apiGroups")

    api_versions: list[str] | None = Field(None, alias="apiVersions")

    operations: list[str] | None = Field(None, alias="operations")

    resources: list[str] | None = Field(None, alias="resources")

    scope: str | None = Field(None, alias="scope")
