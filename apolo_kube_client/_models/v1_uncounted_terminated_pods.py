from pydantic import BaseModel
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1UncountedTerminatedPods",)


class V1UncountedTerminatedPods(BaseModel):
    failed: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []

    succeeded: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []
