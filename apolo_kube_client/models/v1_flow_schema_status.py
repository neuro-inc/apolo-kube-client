from pydantic import BaseModel
from .v1_flow_schema_condition import V1FlowSchemaCondition

__all__ = ("V1FlowSchemaStatus",)


class V1FlowSchemaStatus(BaseModel):
    conditions: list[V1FlowSchemaCondition] = []
