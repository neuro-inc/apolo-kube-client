from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field


__all__ = ("V1ResourceRule",)


class V1ResourceRule(BaseModel):
    api_groups: list[str] = Field(
        default=[],
        serialization_alias="apiGroups",
        validation_alias=AliasChoices("api_groups", "apiGroups"),
    )

    resource_names: list[str] = Field(
        default=[],
        serialization_alias="resourceNames",
        validation_alias=AliasChoices("resource_names", "resourceNames"),
    )

    resources: list[str] = Field(default=[])

    verbs: list[str] = Field(default=[])
