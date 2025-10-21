from pydantic import BaseModel
from .utils import _collection_if_none
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1HostAlias",)


class V1HostAlias(BaseModel):
    hostnames: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = []

    ip: str | None = None
