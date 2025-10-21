from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .v1beta2_capacity_request_policy_range import V1beta2CapacityRequestPolicyRange
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta2CapacityRequestPolicy",)


class V1beta2CapacityRequestPolicy(BaseModel):
    default: str | None = None

    valid_range: Annotated[
        V1beta2CapacityRequestPolicyRange,
        BeforeValidator(_default_if_none(V1beta2CapacityRequestPolicyRange)),
    ] = Field(
        default_factory=lambda: V1beta2CapacityRequestPolicyRange(),
        serialization_alias="validRange",
        validation_alias=AliasChoices("valid_range", "validRange"),
    )

    valid_values: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="validValues",
            validation_alias=AliasChoices("valid_values", "validValues"),
        )
    )
