from pydantic import BaseModel, Field

from .v1_success_policy_rule import V1SuccessPolicyRule


class V1SuccessPolicy(BaseModel):
    rules: list[V1SuccessPolicyRule] | None = Field(None, alias="rules")
