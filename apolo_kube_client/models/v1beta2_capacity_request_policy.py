from __future__ import annotations
from pydantic import BaseModel, Field
from .v1beta2_capacity_request_policy_range import V1beta2CapacityRequestPolicyRange

__all__ = ("V1beta2CapacityRequestPolicy",)


class V1beta2CapacityRequestPolicy(BaseModel):
    default: str | None = Field(default_factory=lambda: None, alias="default")

    valid_range: V1beta2CapacityRequestPolicyRange = Field(
        default_factory=lambda: V1beta2CapacityRequestPolicyRange(), alias="validRange"
    )

    valid_values: list[str] = Field(default_factory=lambda: [], alias="validValues")
