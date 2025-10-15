from pydantic import BaseModel, Field

from .v1_priority_level_configuration_condition import (
    V1PriorityLevelConfigurationCondition,
)


class V1PriorityLevelConfigurationStatus(BaseModel):
    conditions: list[V1PriorityLevelConfigurationCondition] | None = Field(
        None, alias="conditions"
    )
