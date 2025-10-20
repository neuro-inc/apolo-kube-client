from pydantic import AliasChoices, BaseModel, Field
from .v1_api_group import V1APIGroup

__all__ = ("V1APIGroupList",)


class V1APIGroupList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    groups: list[V1APIGroup] = []

    kind: str | None = None
