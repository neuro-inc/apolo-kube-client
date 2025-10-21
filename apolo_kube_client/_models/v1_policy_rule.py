from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1PolicyRule",)


class V1PolicyRule(BaseModel):
    api_groups: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="apiGroups",
            validation_alias=AliasChoices("api_groups", "apiGroups"),
        )
    )

    non_resource_ur_ls: Annotated[
        list[str], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="nonResourceURLs",
        validation_alias=AliasChoices("non_resource_ur_ls", "nonResourceURLs"),
    )

    resource_names: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="resourceNames",
            validation_alias=AliasChoices("resource_names", "resourceNames"),
        )
    )

    resources: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []

    verbs: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []
