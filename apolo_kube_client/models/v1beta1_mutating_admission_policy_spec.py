from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta1_match_condition import V1beta1MatchCondition
from .v1beta1_match_resources import V1beta1MatchResources
from .v1beta1_mutation import V1beta1Mutation
from .v1beta1_param_kind import V1beta1ParamKind
from .v1beta1_variable import V1beta1Variable

__all__ = ("V1beta1MutatingAdmissionPolicySpec",)


class V1beta1MutatingAdmissionPolicySpec(BaseModel):
    failure_policy: str | None = Field(
        default_factory=lambda: None, alias="failurePolicy"
    )

    match_conditions: list[V1beta1MatchCondition] = Field(
        default_factory=lambda: [], alias="matchConditions"
    )

    match_constraints: V1beta1MatchResources = Field(
        default_factory=lambda: V1beta1MatchResources(), alias="matchConstraints"
    )

    mutations: list[V1beta1Mutation] = Field(default_factory=lambda: [])

    param_kind: V1beta1ParamKind = Field(
        default_factory=lambda: V1beta1ParamKind(), alias="paramKind"
    )

    reinvocation_policy: str | None = Field(
        default_factory=lambda: None, alias="reinvocationPolicy"
    )

    variables: list[V1beta1Variable] = Field(default_factory=lambda: [])
