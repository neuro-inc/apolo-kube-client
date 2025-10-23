from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1APIResource",)


class V1APIResource(BaseModel):
    categories: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(default=[], exclude_if=_exclude_if)
    )

    group: str | None = Field(default=None, exclude_if=_exclude_if)

    kind: str | None = Field(default=None, exclude_if=_exclude_if)

    name: str | None = Field(default=None, exclude_if=_exclude_if)

    namespaced: bool | None = Field(default=None, exclude_if=_exclude_if)

    short_names: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="shortNames",
            validation_alias=AliasChoices("short_names", "shortNames"),
            exclude_if=_exclude_if,
        )
    )

    singular_name: str | None = Field(
        default=None,
        serialization_alias="singularName",
        validation_alias=AliasChoices("singular_name", "singularName"),
        exclude_if=_exclude_if,
    )

    storage_version_hash: str | None = Field(
        default=None,
        serialization_alias="storageVersionHash",
        validation_alias=AliasChoices("storage_version_hash", "storageVersionHash"),
        exclude_if=_exclude_if,
    )

    verbs: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[], exclude_if=_exclude_if
    )

    version: str | None = Field(default=None, exclude_if=_exclude_if)
