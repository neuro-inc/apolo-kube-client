from pydantic import BaseModel, Field

from .v1_flow_schema_condition import V1FlowSchemaCondition


class V1FlowSchemaStatus(BaseModel):
    conditions: list[V1FlowSchemaCondition] | None = Field(None, alias="conditions")
