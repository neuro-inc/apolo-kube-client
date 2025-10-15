from pydantic import BaseModel, Field

from .v1beta1_match_resources import V1beta1MatchResources
from .v1beta1_param_ref import V1beta1ParamRef


class V1beta1ValidatingAdmissionPolicyBindingSpec(BaseModel):
    match_resources: V1beta1MatchResources | None = Field(None, alias="matchResources")

    param_ref: V1beta1ParamRef | None = Field(None, alias="paramRef")

    policy_name: str | None = Field(None, alias="policyName")

    validation_actions: list[str] | None = Field(None, alias="validationActions")
