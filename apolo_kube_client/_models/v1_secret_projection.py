from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_key_to_path import V1KeyToPath
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1SecretProjection",)


class V1SecretProjection(BaseModel):
    items: Annotated[list[V1KeyToPath], BeforeValidator(_collection_if_none("[]"))] = (
        Field(default=[], exclude_if=_exclude_if)
    )

    name: str | None = Field(default=None, exclude_if=_exclude_if)

    optional: bool | None = Field(default=None, exclude_if=_exclude_if)
