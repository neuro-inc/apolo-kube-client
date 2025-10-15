from pydantic import BaseModel, Field

from .v1_condition import V1Condition


class V1beta1ServiceCIDRStatus(BaseModel):
    conditions: list[V1Condition] | None = Field(None, alias="conditions")
