from pydantic import BaseModel
from .v1_priority_level_configuration_condition import (
    V1PriorityLevelConfigurationCondition,
)

__all__ = ("V1PriorityLevelConfigurationStatus",)


class V1PriorityLevelConfigurationStatus(BaseModel):
    conditions: list[V1PriorityLevelConfigurationCondition] = []
