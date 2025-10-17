from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1NonResourcePolicyRule",)


class V1NonResourcePolicyRule(BaseModel):
    non_resource_ur_ls: list[str] = Field(
        default=[],
        serialization_alias="nonResourceURLs",
        validation_alias=AliasChoices("non_resource_ur_ls", "nonResourceURLs"),
    )

    verbs: list[str] = []
