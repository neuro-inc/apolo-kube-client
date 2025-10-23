from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1LabelSelectorRequirement",)


class V1LabelSelectorRequirement(BaseModel):
    key: str | None = Field(default=None, exclude_if=_exclude_if)

    operator: str | None = Field(default=None, exclude_if=_exclude_if)

    values: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[], exclude_if=_exclude_if
    )
