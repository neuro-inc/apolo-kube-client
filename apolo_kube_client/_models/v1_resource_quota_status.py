from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ResourceQuotaStatus",)


class V1ResourceQuotaStatus(BaseModel):
    hard: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = Field(
        default={}, exclude_if=_exclude_if
    )

    used: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = Field(
        default={}, exclude_if=_exclude_if
    )
