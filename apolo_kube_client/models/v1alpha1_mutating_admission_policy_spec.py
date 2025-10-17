from __future__ import annotations
from pydantic import BaseModel, Field
from .v1alpha1_match_condition import V1alpha1MatchCondition
from .v1alpha1_match_resources import V1alpha1MatchResources
from .v1alpha1_mutation import V1alpha1Mutation
from .v1alpha1_param_kind import V1alpha1ParamKind
from .v1alpha1_variable import V1alpha1Variable

__all__ = ("V1alpha1MutatingAdmissionPolicySpec",)


class V1alpha1MutatingAdmissionPolicySpec(BaseModel):
    failure_policy: str | None = Field(
        default_factory=lambda: None, alias="failurePolicy"
    )

    match_conditions: list[V1alpha1MatchCondition] = Field(
        default_factory=lambda: [], alias="matchConditions"
    )

    match_constraints: V1alpha1MatchResources = Field(
        default_factory=lambda: V1alpha1MatchResources(), alias="matchConstraints"
    )

    mutations: list[V1alpha1Mutation] = Field(default_factory=lambda: [])

    param_kind: V1alpha1ParamKind = Field(
        default_factory=lambda: V1alpha1ParamKind(), alias="paramKind"
    )

    reinvocation_policy: str | None = Field(
        default_factory=lambda: None, alias="reinvocationPolicy"
    )

    variables: list[V1alpha1Variable] = Field(default_factory=lambda: [])
