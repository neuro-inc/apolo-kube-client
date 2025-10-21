from pydantic import BaseModel
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1UserInfo",)


class V1UserInfo(BaseModel):
    extra: Annotated[
        dict[str, list[str]], BeforeValidator(_collection_if_none("{}"))
    ] = {}

    groups: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []

    uid: str | None = None

    username: str | None = None
