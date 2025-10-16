from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_flow_distinguisher_method import V1FlowDistinguisherMethod
from .v1_policy_rules_with_subjects import V1PolicyRulesWithSubjects
from .v1_priority_level_configuration_reference import (
    V1PriorityLevelConfigurationReference,
)

__all__ = ("V1FlowSchemaSpec",)


class V1FlowSchemaSpec(BaseModel):
    distinguisher_method: V1FlowDistinguisherMethod = Field(
        default_factory=lambda: V1FlowDistinguisherMethod(), alias="distinguisherMethod"
    )

    matching_precedence: int | None = Field(
        default_factory=lambda: None, alias="matchingPrecedence"
    )

    priority_level_configuration: V1PriorityLevelConfigurationReference = Field(
        default_factory=lambda: V1PriorityLevelConfigurationReference(),
        alias="priorityLevelConfiguration",
    )

    rules: list[V1PolicyRulesWithSubjects] = Field(
        default_factory=lambda: [], alias="rules"
    )
