from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1beta1_match_resources import V1beta1MatchResources
from .v1beta1_param_ref import V1beta1ParamRef
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1MutatingAdmissionPolicyBindingSpec",)


class V1beta1MutatingAdmissionPolicyBindingSpec(BaseModel):
    match_resources: Annotated[
        V1beta1MatchResources, BeforeValidator(_default_if_none(V1beta1MatchResources))
    ] = Field(
        default_factory=lambda: V1beta1MatchResources(),
        serialization_alias="matchResources",
        validation_alias=AliasChoices("match_resources", "matchResources"),
        exclude_if=_exclude_if,
    )

    param_ref: Annotated[
        V1beta1ParamRef, BeforeValidator(_default_if_none(V1beta1ParamRef))
    ] = Field(
        default_factory=lambda: V1beta1ParamRef(),
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
