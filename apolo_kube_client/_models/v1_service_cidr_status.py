from pydantic import BaseModel
from .utils import _collection_if_none
from .v1_condition import V1Condition
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1ServiceCIDRStatus",)


class V1ServiceCIDRStatus(BaseModel):
    conditions: Annotated[
        list[V1Condition], BeforeValidator(_collection_if_none("[]"))
    ] = []
