from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_success_policy_rule import V1SuccessPolicyRule

__all__ = ("V1SuccessPolicy",)


class V1SuccessPolicy(BaseModel):
    rules: list[V1SuccessPolicyRule] = Field(default_factory=lambda: [], alias="rules")
