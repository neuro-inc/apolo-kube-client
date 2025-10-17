from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_exempt_priority_level_configuration import V1ExemptPriorityLevelConfiguration
from .v1_limited_priority_level_configuration import V1LimitedPriorityLevelConfiguration

__all__ = ("V1PriorityLevelConfigurationSpec",)


class V1PriorityLevelConfigurationSpec(BaseModel):
    exempt: V1ExemptPriorityLevelConfiguration = Field(
        default_factory=lambda: V1ExemptPriorityLevelConfiguration()
    )

    limited: V1LimitedPriorityLevelConfiguration = Field(
        default_factory=lambda: V1LimitedPriorityLevelConfiguration()
    )

    type: str | None = Field(default_factory=lambda: None)
