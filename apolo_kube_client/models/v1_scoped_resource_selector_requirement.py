from pydantic import BaseModel, Field


class V1ScopedResourceSelectorRequirement(BaseModel):
    operator: str | None = Field(None, alias="operator")

    scope_name: str | None = Field(None, alias="scopeName")

    values: list[str] | None = Field(None, alias="values")
