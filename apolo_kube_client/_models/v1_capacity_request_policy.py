from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _default_if_none
from .utils import _exclude_if
from .v1_capacity_request_policy_range import V1CapacityRequestPolicyRange
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1CapacityRequestPolicy",)


class V1CapacityRequestPolicy(BaseModel):
    default: str | None = Field(default=None, exclude_if=_exclude_if)

    valid_range: Annotated[
        V1CapacityRequestPolicyRange,
        BeforeValidator(_default_if_none(V1CapacityRequestPolicyRange)),
    ] = Field(
        default_factory=lambda: V1CapacityRequestPolicyRange(),
        serialization_alias="validRange",
        validation_alias=AliasChoices("valid_range", "validRange"),
        exclude_if=_exclude_if,
    )

    valid_values: Annotated[list[str], BeforeValidator(_collection_if_none("[]"))] = (
        Field(
            default=[],
            serialization_alias="validValues",
            validation_alias=AliasChoices("valid_values", "validValues"),
            exclude_if=_exclude_if,
        )
    )
