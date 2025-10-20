from pydantic import AliasChoices, BaseModel, Field
from .v1beta2_capacity_request_policy_range import V1beta2CapacityRequestPolicyRange

__all__ = ("V1beta2CapacityRequestPolicy",)


class V1beta2CapacityRequestPolicy(BaseModel):
    default: str | None = None

    valid_range: V1beta2CapacityRequestPolicyRange = Field(
        default_factory=lambda: V1beta2CapacityRequestPolicyRange(),
        serialization_alias="validRange",
        validation_alias=AliasChoices("valid_range", "validRange"),
    )

    valid_values: list[str] = Field(
        default=[],
        serialization_alias="validValues",
        validation_alias=AliasChoices("valid_values", "validValues"),
    )
