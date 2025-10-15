from pydantic import BaseModel, Field

from .v1_flow_distinguisher_method import V1FlowDistinguisherMethod
from .v1_policy_rules_with_subjects import V1PolicyRulesWithSubjects
from .v1_priority_level_configuration_reference import (
    V1PriorityLevelConfigurationReference,
)


class V1FlowSchemaSpec(BaseModel):
    distinguisher_method: V1FlowDistinguisherMethod | None = Field(
        None, alias="distinguisherMethod"
    )

    matching_precedence: int | None = Field(None, alias="matchingPrecedence")

    priority_level_configuration: V1PriorityLevelConfigurationReference | None = Field(
        None, alias="priorityLevelConfiguration"
    )

    rules: list[V1PolicyRulesWithSubjects] | None = Field(None, alias="rules")
