from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_condition import V1Condition
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ServiceCIDRStatus",)


class V1ServiceCIDRStatus(BaseModel):
    conditions: Annotated[
        list[V1Condition], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)
