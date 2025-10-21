from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CustomResourceDefinitionNames",)


class V1CustomResourceDefinitionNames(BaseModel):
    categories: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []

    kind: str | None = None

    list_kind: str | None = Field(
        default=None,
        serialization_alias="listKind",
        validation_alias=AliasChoices("list_kind", "listKind"),
    )

    plural: str | None = None

    short_names: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="shortNames",
            validation_alias=AliasChoices("short_names", "shortNames"),
        )
    )

    singular: str | None = None
