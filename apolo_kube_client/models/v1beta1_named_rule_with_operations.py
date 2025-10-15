from pydantic import BaseModel, Field


class V1beta1NamedRuleWithOperations(BaseModel):
    api_groups: list[str] | None = Field(None, alias="apiGroups")

    api_versions: list[str] | None = Field(None, alias="apiVersions")

    operations: list[str] | None = Field(None, alias="operations")

    resource_names: list[str] | None = Field(None, alias="resourceNames")

    resources: list[str] | None = Field(None, alias="resources")

    scope: str | None = Field(None, alias="scope")
