from pydantic import BaseModel, Field

from .v1_a_p_i_service_condition import V1APIServiceCondition


class V1APIServiceStatus(BaseModel):
    conditions: list[V1APIServiceCondition] | None = Field(None, alias="conditions")
