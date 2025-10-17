from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1ResourcePolicyRule",)


class V1ResourcePolicyRule(BaseModel):
    api_groups: list[str] = Field(
        default=[],
        serialization_alias="apiGroups",
        validation_alias=AliasChoices("api_groups", "apiGroups"),
    )

    cluster_scope: bool | None = Field(
        default=None,
        serialization_alias="clusterScope",
        validation_alias=AliasChoices("cluster_scope", "clusterScope"),
    )

    namespaces: list[str] = []

    resources: list[str] = []

    verbs: list[str] = []
