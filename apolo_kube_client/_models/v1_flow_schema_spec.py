from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
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
        exclude_if=_exclude_if,
    )

    matching_precedence: int | None = Field(
        default=None,
        serialization_alias="matchingPrecedence",
        validation_alias=AliasChoices("matching_precedence", "matchingPrecedence"),
        exclude_if=_exclude_if,
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
        exclude_if=_exclude_if,
    )

    rules: Annotated[
        list[V1PolicyRulesWithSubjects], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)
