from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta1_match_resources import V1beta1MatchResources
from .v1beta1_param_ref import V1beta1ParamRef

__all__ = ("V1beta1MutatingAdmissionPolicyBindingSpec",)


class V1beta1MutatingAdmissionPolicyBindingSpec(BaseModel):
    match_resources: V1beta1MatchResources = Field(
        default_factory=lambda: V1beta1MatchResources(), alias="matchResources"
    )

    param_ref: V1beta1ParamRef = Field(
        default_factory=lambda: V1beta1ParamRef(), alias="paramRef"
    )

    policy_name: str | None = Field(default_factory=lambda: None, alias="policyName")
