from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1_api_group import V1APIGroup
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1APIGroupList",)


class V1APIGroupList(BaseModel):
    api_version: str | None = Field(
        default=None,
        serialization_alias="apiVersion",
        validation_alias=AliasChoices("api_version", "apiVersion"),
    )

    groups: Annotated[list[V1APIGroup], BeforeValidator(_collection_if_none("[]"))] = []

    kind: str | None = None
