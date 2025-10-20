from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1PolicyRule",)


class V1PolicyRule(BaseModel):
    api_groups: list[str] = Field(
        default=[],
        serialization_alias="apiGroups",
        validation_alias=AliasChoices("api_groups", "apiGroups"),
    )

    non_resource_ur_ls: list[str] = Field(
        default=[],
        serialization_alias="nonResourceURLs",
        validation_alias=AliasChoices("non_resource_ur_ls", "nonResourceURLs"),
    )

    resource_names: list[str] = Field(
        default=[],
        serialization_alias="resourceNames",
        validation_alias=AliasChoices("resource_names", "resourceNames"),
    )

    resources: list[str] = []

    verbs: list[str] = []
