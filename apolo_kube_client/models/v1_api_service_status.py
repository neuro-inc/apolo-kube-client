from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_api_service_condition import V1APIServiceCondition

__all__ = ("V1APIServiceStatus",)


class V1APIServiceStatus(BaseModel):
    conditions: list[V1APIServiceCondition] = Field(default=[])
