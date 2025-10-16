from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_match_resources import V1MatchResources
from .v1_param_ref import V1ParamRef

__all__ = ("V1ValidatingAdmissionPolicyBindingSpec",)


class V1ValidatingAdmissionPolicyBindingSpec(BaseModel):
    match_resources: V1MatchResources = Field(
        default_factory=lambda: V1MatchResources(), alias="matchResources"
    )

    param_ref: V1ParamRef = Field(
        default_factory=lambda: V1ParamRef(), alias="paramRef"
    )

    policy_name: str | None = Field(default_factory=lambda: None, alias="policyName")

    validation_actions: list[str] = Field(
        default_factory=lambda: [], alias="validationActions"
    )
