from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CustomResourceDefinitionNames",)


class V1CustomResourceDefinitionNames(BaseModel):
    categories: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(default=[], exclude_if=_exclude_if)
    )

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    list_kind: str | None = Field(
        default=None,
        serialization_alias="listKind",
        validation_alias=AliasChoices("list_kind", "listKind"),
        exclude_if=_exclude_if,
    )

    plural: str | None = Field(default=None, exclude_if=_exclude_if)

    short_names: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="shortNames",
            validation_alias=AliasChoices("short_names", "shortNames"),
            exclude_if=_exclude_if,
        )
    )

    singular: str | None = Field(default=None, exclude_if=_exclude_if)
