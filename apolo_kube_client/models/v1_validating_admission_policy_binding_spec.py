from pydantic import BaseModel, Field

from .v1_match_resources import V1MatchResources
from .v1_param_ref import V1ParamRef


class V1ValidatingAdmissionPolicyBindingSpec(BaseModel):
    match_resources: V1MatchResources | None = Field(None, alias="matchResources")

    param_ref: V1ParamRef | None = Field(None, alias="paramRef")

    policy_name: str | None = Field(None, alias="policyName")

    validation_actions: list[str] | None = Field(None, alias="validationActions")
