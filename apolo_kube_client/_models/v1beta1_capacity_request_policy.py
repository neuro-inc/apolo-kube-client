from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1beta1_capacity_request_policy_range import V1beta1CapacityRequestPolicyRange
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1CapacityRequestPolicy",)


class V1beta1CapacityRequestPolicy(BaseModel):
    default: str | None = None

    valid_range: Annotated[
        V1beta1CapacityRequestPolicyRange,
        BeforeValidator(_default_if_none(V1beta1CapacityRequestPolicyRange)),
    ] = Field(
        default_factory=lambda: V1beta1CapacityRequestPolicyRange(),
        serialization_alias="validRange",
        validation_alias=AliasChoices("valid_range", "validRange"),
    )

    valid_values: list[str] = Field(
        default=[],
        serialization_alias="validValues",
        validation_alias=AliasChoices("valid_values", "validValues"),
    )
