from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_flow_distinguisher_method import V1FlowDistinguisherMethod
from .v1_policy_rules_with_subjects import V1PolicyRulesWithSubjects
from .v1_priority_level_configuration_reference import (
    V1PriorityLevelConfigurationReference,
)
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1FlowSchemaSpec",)


class V1FlowSchemaSpec(BaseModel):
    distinguisher_method: Annotated[
        V1FlowDistinguisherMethod,
        BeforeValidator(_default_if_none(V1FlowDistinguisherMethod)),
    ] = Field(
        default_factory=lambda: V1FlowDistinguisherMethod(),
        serialization_alias="distinguisherMethod",
        validation_alias=AliasChoices("distinguisher_method", "distinguisherMethod"),
    )

    matching_precedence: int | None = Field(
        default=None,
        serialization_alias="matchingPrecedence",
        validation_alias=AliasChoices("matching_precedence", "matchingPrecedence"),
    )

    priority_level_configuration: Annotated[
        V1PriorityLevelConfigurationReference,
        BeforeValidator(_default_if_none(V1PriorityLevelConfigurationReference)),
    ] = Field(
        default_factory=lambda: V1PriorityLevelConfigurationReference(),
        serialization_alias="priorityLevelConfiguration",
        validation_alias=AliasChoices(
            "priority_level_configuration", "priorityLevelConfiguration"
        ),
    )

    rules: list[V1PolicyRulesWithSubjects] = []
