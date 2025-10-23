from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_api_service_condition import V1APIServiceCondition
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1APIServiceStatus",)


class V1APIServiceStatus(BaseModel):
    conditions: Annotated[
        list[V1APIServiceCondition], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)
