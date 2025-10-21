from pydantic import BaseModel
from .utils import _collection_if_none
from .v1_flow_schema_condition import V1FlowSchemaCondition
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1FlowSchemaStatus",)


class V1FlowSchemaStatus(BaseModel):
    conditions: Annotated[
        list[V1FlowSchemaCondition], BeforeValidator(_collection_if_none("[]"))
    ] = []
