from pydantic import BaseModel, Field


class V1ResourceRule(BaseModel):
    api_groups: list[str] | None = Field(None, alias="apiGroups")

    resource_names: list[str] | None = Field(None, alias="resourceNames")

    resources: list[str] | None = Field(None, alias="resources")

    verbs: list[str] | None = Field(None, alias="verbs")
