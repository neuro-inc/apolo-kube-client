from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1_api_resource import V1APIResource

__all__ = ("V1APIResourceList",)


class V1APIResourceList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    group_version: str | None = Field(
        default=None,
        serialization_alias="groupVersion",
        validation_alias=AliasChoices("group_version", "groupVersion"),
    )

    kind: str | None = Field(default=None)

    resources: list[V1APIResource] = Field(default=[])
