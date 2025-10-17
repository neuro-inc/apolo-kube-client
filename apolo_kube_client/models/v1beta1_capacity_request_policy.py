from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta1_capacity_request_policy_range import V1beta1CapacityRequestPolicyRange

__all__ = ("V1beta1CapacityRequestPolicy",)


class V1beta1CapacityRequestPolicy(BaseModel):
    default: str | None = Field(default_factory=lambda: None)

    valid_range: V1beta1CapacityRequestPolicyRange = Field(
        default_factory=lambda: V1beta1CapacityRequestPolicyRange(), alias="validRange"
    )

    valid_values: list[str] = Field(default_factory=lambda: [], alias="validValues")
