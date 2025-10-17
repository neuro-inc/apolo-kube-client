from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_flow_schema_condition import V1FlowSchemaCondition

__all__ = ("V1FlowSchemaStatus",)


class V1FlowSchemaStatus(BaseModel):
    conditions: list[V1FlowSchemaCondition] = Field(default_factory=lambda: [])
