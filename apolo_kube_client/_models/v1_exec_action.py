from pydantic import BaseModel
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ExecAction",)


class V1ExecAction(BaseModel):
    command: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []
