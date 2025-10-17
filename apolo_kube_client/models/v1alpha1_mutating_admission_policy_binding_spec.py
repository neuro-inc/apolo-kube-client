from pydantic import AliasChoices, BaseModel, Field
from .v1alpha1_match_resources import V1alpha1MatchResources
from .v1alpha1_param_ref import V1alpha1ParamRef

__all__ = ("V1alpha1MutatingAdmissionPolicyBindingSpec",)


class V1alpha1MutatingAdmissionPolicyBindingSpec(BaseModel):
    match_resources: V1alpha1MatchResources = Field(
        default_factory=lambda: V1alpha1MatchResources(),
        serialization_alias="matchResources",
        validation_alias=AliasChoices("match_resources", "matchResources"),
    )

    param_ref: V1alpha1ParamRef = Field(
        default_factory=lambda: V1alpha1ParamRef(),
        serialization_alias="paramRef",
        validation_alias=AliasChoices("param_ref", "paramRef"),
    )

    policy_name: str | None = Field(
        default=None,
        serialization_alias="policyName",
        validation_alias=AliasChoices("policy_name", "policyName"),
    )
