from __future__ import annotations

from pydantic import BaseModel, Field

from .v1alpha1_match_resources import V1alpha1MatchResources
from .v1alpha1_param_ref import V1alpha1ParamRef

__all__ = ("V1alpha1MutatingAdmissionPolicyBindingSpec",)


class V1alpha1MutatingAdmissionPolicyBindingSpec(BaseModel):
    match_resources: V1alpha1MatchResources | None = Field(None, alias="matchResources")

    param_ref: V1alpha1ParamRef | None = Field(None, alias="paramRef")

    policy_name: str | None = Field(None, alias="policyName")
