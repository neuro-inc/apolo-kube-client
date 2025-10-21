from pydantic import BaseModel
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1LabelSelectorRequirement",)


class V1LabelSelectorRequirement(BaseModel):
    key: str | None = None

    operator: str | None = None

    values: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []
