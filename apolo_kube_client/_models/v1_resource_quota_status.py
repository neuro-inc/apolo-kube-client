from pydantic import BaseModel
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ResourceQuotaStatus",)


class V1ResourceQuotaStatus(BaseModel):
    hard: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = {}

    used: Annotated[dict[str, str], BeforeValidator(_collection_if_none("{}"))] = {}
