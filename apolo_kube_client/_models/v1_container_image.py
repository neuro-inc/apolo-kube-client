from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ContainerImage",)


class V1ContainerImage(BaseModel):
    names: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []

    size_bytes: int | None = Field(
        default=None,
        serialization_alias="sizeBytes",
        validation_alias=AliasChoices("size_bytes", "sizeBytes"),
    )
