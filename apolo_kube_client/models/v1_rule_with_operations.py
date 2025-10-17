from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1RuleWithOperations",)


class V1RuleWithOperations(BaseModel):
    api_groups: list[str] = Field(
        default=[],
        serialization_alias="apiGroups",
        validation_alias=AliasChoices("api_groups", "apiGroups"),
    )

    api_versions: list[str] = Field(
        default=[],
        serialization_alias="apiVersions",
        validation_alias=AliasChoices("api_versions", "apiVersions"),
    )

    operations: list[str] = []

    resources: list[str] = []

    scope: str | None = None
