from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1alpha1_match_condition import V1alpha1MatchCondition
from .v1alpha1_match_resources import V1alpha1MatchResources
from .v1alpha1_mutation import V1alpha1Mutation
from .v1alpha1_param_kind import V1alpha1ParamKind
from .v1alpha1_variable import V1alpha1Variable

__all__ = ("V1alpha1MutatingAdmissionPolicySpec",)


class V1alpha1MutatingAdmissionPolicySpec(BaseModel):
    failure_policy: str | None = Field(
        default=None,
        serialization_alias="failurePolicy",
        validation_alias=AliasChoices("failure_policy", "failurePolicy"),
    )

    match_conditions: list[V1alpha1MatchCondition] = Field(
        default=[],
        serialization_alias="matchConditions",
        validation_alias=AliasChoices("match_conditions", "matchConditions"),
    )

    match_constraints: V1alpha1MatchResources = Field(
        default_factory=lambda: V1alpha1MatchResources(),
        serialization_alias="matchConstraints",
        validation_alias=AliasChoices("match_constraints", "matchConstraints"),
    )

    mutations: list[V1alpha1Mutation] = Field(default=[])

    param_kind: V1alpha1ParamKind = Field(
        default_factory=lambda: V1alpha1ParamKind(),
        serialization_alias="paramKind",
        validation_alias=AliasChoices("param_kind", "paramKind"),
    )

    reinvocation_policy: str | None = Field(
        default=None,
        serialization_alias="reinvocationPolicy",
        validation_alias=AliasChoices("reinvocation_policy", "reinvocationPolicy"),
    )

    variables: list[V1alpha1Variable] = Field(default=[])
