from pydantic import BaseModel
from .v1_condition import V1Condition

__all__ = ("V1beta1ServiceCIDRStatus",)


class V1beta1ServiceCIDRStatus(BaseModel):
    conditions: list[V1Condition] = []
