from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1beta1_match_condition import V1beta1MatchCondition
from .v1beta1_match_resources import V1beta1MatchResources
from .v1beta1_mutation import V1beta1Mutation
from .v1beta1_param_kind import V1beta1ParamKind
from .v1beta1_variable import V1beta1Variable

__all__ = ("V1beta1MutatingAdmissionPolicySpec",)


class V1beta1MutatingAdmissionPolicySpec(BaseModel):
    failure_policy: str | None = Field(
        default=None,
        serialization_alias="failurePolicy",
        validation_alias=AliasChoices("failure_policy", "failurePolicy"),
    )

    match_conditions: list[V1beta1MatchCondition] = Field(
        default=[],
        serialization_alias="matchConditions",
        validation_alias=AliasChoices("match_conditions", "matchConditions"),
    )

    match_constraints: V1beta1MatchResources = Field(
        default_factory=lambda: V1beta1MatchResources(),
        serialization_alias="matchConstraints",
        validation_alias=AliasChoices("match_constraints", "matchConstraints"),
    )

    mutations: list[V1beta1Mutation] = Field(default=[])

    param_kind: V1beta1ParamKind = Field(
        default_factory=lambda: V1beta1ParamKind(),
        serialization_alias="paramKind",
        validation_alias=AliasChoices("param_kind", "paramKind"),
    )

    reinvocation_policy: str | None = Field(
        default=None,
        serialization_alias="reinvocationPolicy",
        validation_alias=AliasChoices("reinvocation_policy", "reinvocationPolicy"),
    )

    variables: list[V1beta1Variable] = Field(default=[])
