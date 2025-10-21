from pydantic import BaseModel
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1NamespaceSpec",)


class V1NamespaceSpec(BaseModel):
    finalizers: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []
