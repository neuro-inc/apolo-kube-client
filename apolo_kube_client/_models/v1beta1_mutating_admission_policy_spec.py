from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1beta1_match_condition import V1beta1MatchCondition
from .v1beta1_match_resources import V1beta1MatchResources
from .v1beta1_mutation import V1beta1Mutation
from .v1beta1_param_kind import V1beta1ParamKind
from .v1beta1_variable import V1beta1Variable
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1MutatingAdmissionPolicySpec",)


class V1beta1MutatingAdmissionPolicySpec(BaseModel):
    failure_policy: str | None = Field(
        default=None,
        serialization_alias="failurePolicy",
        validation_alias=AliasChoices("failure_policy", "failurePolicy"),
    )

    match_conditions: Annotated[
        list[V1beta1MatchCondition], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="matchConditions",
        validation_alias=AliasChoices("match_conditions", "matchConditions"),
    )

    match_constraints: Annotated[
        V1beta1MatchResources, BeforeValidator(_default_if_none(V1beta1MatchResources))
    ] = Field(
        default_factory=lambda: V1beta1MatchResources(),
        serialization_alias="matchConstraints",
        validation_alias=AliasChoices("match_constraints", "matchConstraints"),
    )

    mutations: Annotated[
        list[V1beta1Mutation], BeforeValidator(_collection_if_none("[]"))
    ] = []

    param_kind: Annotated[
        V1beta1ParamKind, BeforeValidator(_default_if_none(V1beta1ParamKind))
    ] = Field(
        default_factory=lambda: V1beta1ParamKind(),
        serialization_alias="paramKind",
        validation_alias=AliasChoices("param_kind", "paramKind"),
    )

    reinvocation_policy: str | None = Field(
        default=None,
        serialization_alias="reinvocationPolicy",
        validation_alias=AliasChoices("reinvocation_policy", "reinvocationPolicy"),
    )

    variables: Annotated[
        list[V1beta1Variable], BeforeValidator(_collection_if_none("[]"))
    ] = []
