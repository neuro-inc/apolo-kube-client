from pydantic import BaseModel
from .v1_success_policy_rule import V1SuccessPolicyRule

__all__ = ("V1SuccessPolicy",)


class V1SuccessPolicy(BaseModel):
    rules: list[V1SuccessPolicyRule] = []
