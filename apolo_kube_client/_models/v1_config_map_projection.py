from pydantic import BaseModel
from .utils import _collection_if_none
from .v1_key_to_path import V1KeyToPath
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ConfigMapProjection",)


class V1ConfigMapProjection(BaseModel):
    items: Annotated[list[V1KeyToPath], BeforeValidator(_collection_if_none("[]"))] = []

    name: str | None = None

    optional: bool | None = None
