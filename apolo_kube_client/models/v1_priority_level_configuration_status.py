from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_priority_level_configuration_condition import (
    V1PriorityLevelConfigurationCondition,
)

__all__ = ("V1PriorityLevelConfigurationStatus",)


class V1PriorityLevelConfigurationStatus(BaseModel):
    conditions: list[V1PriorityLevelConfigurationCondition] = Field(
        default_factory=lambda: [], alias="conditions"
    )
