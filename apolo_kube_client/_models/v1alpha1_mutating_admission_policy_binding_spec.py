from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1alpha1_match_resources import V1alpha1MatchResources
from .v1alpha1_param_ref import V1alpha1ParamRef
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1alpha1MutatingAdmissionPolicyBindingSpec",)


class V1alpha1MutatingAdmissionPolicyBindingSpec(BaseModel):
    match_resources: Annotated[
        V1alpha1MatchResources,
        BeforeValidator(_default_if_none(V1alpha1MatchResources)),
    ] = Field(
        default_factory=lambda: V1alpha1MatchResources(),
        serialization_alias="matchResources",
        validation_alias=AliasChoices("match_resources", "matchResources"),
        exclude_if=_exclude_if,
    )

    param_ref: Annotated[
        V1alpha1ParamRef, BeforeValidator(_default_if_none(V1alpha1ParamRef))
    ] = Field(
        default_factory=lambda: V1alpha1ParamRef(),
        serialization_alias="paramRef",
        validation_alias=AliasChoices("param_ref", "paramRef"),
        exclude_if=_exclude_if,
    )

    policy_name: str | None = Field(
        default=None,
        serialization_alias="policyName",
        validation_alias=AliasChoices("policy_name", "policyName"),
        exclude_if=_exclude_if,
    )
