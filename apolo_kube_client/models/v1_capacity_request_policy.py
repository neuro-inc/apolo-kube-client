from pydantic import AliasChoices, BaseModel, Field
from .v1_capacity_request_policy_range import V1CapacityRequestPolicyRange

__all__ = ("V1CapacityRequestPolicy",)


class V1CapacityRequestPolicy(BaseModel):
    default: str | None = None

    valid_range: V1CapacityRequestPolicyRange = Field(
        default_factory=lambda: V1CapacityRequestPolicyRange(),
        serialization_alias="validRange",
        validation_alias=AliasChoices("valid_range", "validRange"),
    )

    valid_values: list[str] = Field(
        default=[],
        serialization_alias="validValues",
        validation_alias=AliasChoices("valid_values", "validValues"),
    )
