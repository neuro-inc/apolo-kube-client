from pydantic import AliasChoices, BaseModel, Field
from .v1beta1_match_resources import V1beta1MatchResources
from .v1beta1_param_ref import V1beta1ParamRef

__all__ = ("V1beta1MutatingAdmissionPolicyBindingSpec",)


class V1beta1MutatingAdmissionPolicyBindingSpec(BaseModel):
    match_resources: V1beta1MatchResources = Field(
        default_factory=lambda: V1beta1MatchResources(),
        serialization_alias="matchResources",
        validation_alias=AliasChoices("match_resources", "matchResources"),
    )

    param_ref: V1beta1ParamRef = Field(
        default_factory=lambda: V1beta1ParamRef(),
        serialization_alias="paramRef",
        validation_alias=AliasChoices("param_ref", "paramRef"),
    )

    policy_name: str | None = Field(
        default=None,
        serialization_alias="policyName",
        validation_alias=AliasChoices("policy_name", "policyName"),
    )
