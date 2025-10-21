from pydantic import BaseModel
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1Capabilities",)


class V1Capabilities(BaseModel):
    add: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []

    drop: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []
