from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1NonResourceRule",)


class V1NonResourceRule(BaseModel):
    non_resource_ur_ls: Annotated[
        list[str], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="nonResourceURLs",
        validation_alias=AliasChoices("non_resource_ur_ls", "nonResourceURLs"),
        exclude_if=_exclude_if,
    )

    verbs: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[], exclude_if=_exclude_if
    )
