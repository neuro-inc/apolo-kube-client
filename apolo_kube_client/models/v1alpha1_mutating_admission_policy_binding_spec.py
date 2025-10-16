from __future__ import annotations
from pydantic import BaseModel, Field
from .v1alpha1_match_resources import V1alpha1MatchResources
from .v1alpha1_param_ref import V1alpha1ParamRef

__all__ = ("V1alpha1MutatingAdmissionPolicyBindingSpec",)


class V1alpha1MutatingAdmissionPolicyBindingSpec(BaseModel):
    match_resources: V1alpha1MatchResources = Field(
        default_factory=lambda: V1alpha1MatchResources(), alias="matchResources"
    )

    param_ref: V1alpha1ParamRef = Field(
        default_factory=lambda: V1alpha1ParamRef(), alias="paramRef"
    )

    policy_name: str | None = Field(default_factory=lambda: None, alias="policyName")
