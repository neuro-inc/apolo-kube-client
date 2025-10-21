from pydantic import BaseModel
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1NodeSelectorRequirement",)


class V1NodeSelectorRequirement(BaseModel):
    key: str | None = None

    operator: str | None = None

    values: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []
