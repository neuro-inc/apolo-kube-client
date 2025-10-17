from pydantic import BaseModel
from .v1_condition import V1Condition

__all__ = ("V1ServiceCIDRStatus",)


class V1ServiceCIDRStatus(BaseModel):
    conditions: list[V1Condition] = []
