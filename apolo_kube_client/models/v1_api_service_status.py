from pydantic import BaseModel
from .v1_api_service_condition import V1APIServiceCondition

__all__ = ("V1APIServiceStatus",)


class V1APIServiceStatus(BaseModel):
    conditions: list[V1APIServiceCondition] = []
