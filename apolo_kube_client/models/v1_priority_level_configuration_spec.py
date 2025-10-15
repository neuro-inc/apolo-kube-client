from pydantic import BaseModel, Field

from .v1_exempt_priority_level_configuration import V1ExemptPriorityLevelConfiguration
from .v1_limited_priority_level_configuration import V1LimitedPriorityLevelConfiguration


class V1PriorityLevelConfigurationSpec(BaseModel):
    exempt: V1ExemptPriorityLevelConfiguration | None = Field(None, alias="exempt")

    limited: V1LimitedPriorityLevelConfiguration | None = Field(None, alias="limited")

    type: str | None = Field(None, alias="type")
