from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ContainerImage",)


class V1ContainerImage(BaseModel):
    names: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[], exclude_if=_exclude_if
    )

    size_bytes: int | None = Field(
        default=None,
        serialization_alias="sizeBytes",
        validation_alias=AliasChoices("size_bytes", "sizeBytes"),
        exclude_if=_exclude_if,
    )
