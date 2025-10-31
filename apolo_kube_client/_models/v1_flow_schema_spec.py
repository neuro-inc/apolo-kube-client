from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _collection_if_none
from .v1_flow_distinguisher_method import V1FlowDistinguisherMethod
from .v1_policy_rules_with_subjects import V1PolicyRulesWithSubjects
from .v1_priority_level_configuration_reference import (
    V1PriorityLevelConfigurationReference,
)
from pydantic import BeforeValidator

__all__ = ("V1FlowSchemaSpec",)


class V1FlowSchemaSpec(BaseModel):
    """FlowSchemaSpec describes how the FlowSchema's specification looks like."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.flowcontrol.v1.FlowSchemaSpec"

    distinguisher_method: Annotated[
        V1FlowDistinguisherMethod | None,
        Field(
            alias="distinguisherMethod",
            description="""`distinguisherMethod` defines how to compute the flow distinguisher for requests that match this schema. `nil` specifies that the distinguisher is disabled and thus will always be the empty string.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    matching_precedence: Annotated[
        int | None,
        Field(
            alias="matchingPrecedence",
            description="""`matchingPrecedence` is used to choose among the FlowSchemas that match a given request. The chosen FlowSchema is among those with the numerically lowest (which we take to be logically highest) MatchingPrecedence.  Each MatchingPrecedence value must be ranged in [1,10000]. Note that if the precedence is not specified, it will be set to 1000 as default.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None

    priority_level_configuration: Annotated[
        V1PriorityLevelConfigurationReference,
        Field(
            alias="priorityLevelConfiguration",
            description="""`priorityLevelConfiguration` should reference a PriorityLevelConfiguration in the cluster. If the reference cannot be resolved, the FlowSchema will be ignored and marked as invalid in its status. Required.""",
        ),
    ]

    rules: Annotated[
        list[V1PolicyRulesWithSubjects],
        Field(
            description="""`rules` describes which requests will match this flow schema. This FlowSchema matches a request if and only if at least one member of rules matches the request. if it is an empty slice, there will be no requests matching the FlowSchema.""",
            exclude_if=lambda v: v == [],
        ),
        BeforeValidator(_collection_if_none("[]")),
    ] = []
