from pydantic import BaseModel, Field

from .v1alpha1_match_condition import V1alpha1MatchCondition
from .v1alpha1_match_resources import V1alpha1MatchResources
from .v1alpha1_mutation import V1alpha1Mutation
from .v1alpha1_param_kind import V1alpha1ParamKind
from .v1alpha1_variable import V1alpha1Variable


class V1alpha1MutatingAdmissionPolicySpec(BaseModel):
    failure_policy: str | None = Field(None, alias="failurePolicy")

    match_conditions: list[V1alpha1MatchCondition] | None = Field(
        None, alias="matchConditions"
    )

    match_constraints: V1alpha1MatchResources | None = Field(
        None, alias="matchConstraints"
    )

    mutations: list[V1alpha1Mutation] | None = Field(None, alias="mutations")

    param_kind: V1alpha1ParamKind | None = Field(None, alias="paramKind")

    reinvocation_policy: str | None = Field(None, alias="reinvocationPolicy")

    variables: list[V1alpha1Variable] | None = Field(None, alias="variables")
