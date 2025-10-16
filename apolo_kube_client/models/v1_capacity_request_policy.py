from __future__ import annotations
from pydantic import BaseModel, Field
from .v1_capacity_request_policy_range import V1CapacityRequestPolicyRange

__all__ = ("V1CapacityRequestPolicy",)


class V1CapacityRequestPolicy(BaseModel):
    default: str | None = Field(default_factory=lambda: None, alias="default")

    valid_range: V1CapacityRequestPolicyRange = Field(
        default_factory=lambda: V1CapacityRequestPolicyRange(), alias="validRange"
    )

    valid_values: list[str] = Field(default_factory=lambda: [], alias="validValues")
