from pydantic import BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_flow_schema_condition import V1FlowSchemaCondition
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1FlowSchemaStatus",)


class V1FlowSchemaStatus(BaseModel):
    conditions: Annotated[
        list[V1FlowSchemaCondition], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)
