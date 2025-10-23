from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1HostAlias",)


class V1HostAlias(BaseModel):
    hostnames: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = Field(
        default=[], exclude_if=_exclude_if
    )

    ip: str | None = Field(default=None, exclude_if=_exclude_if)
