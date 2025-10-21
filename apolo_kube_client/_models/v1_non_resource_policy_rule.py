from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1NonResourcePolicyRule",)


class V1NonResourcePolicyRule(BaseModel):
    non_resource_ur_ls: Annotated[
        list[str], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="nonResourceURLs",
        validation_alias=AliasChoices("non_resource_ur_ls", "nonResourceURLs"),
    )

    verbs: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []
