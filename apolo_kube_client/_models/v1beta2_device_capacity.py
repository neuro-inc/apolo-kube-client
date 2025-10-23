from pydantic import AliasChoices, BaseModel, Field
from .utils import _default_if_none
from .utils import _exclude_if
from .v1beta2_capacity_request_policy import V1beta2CapacityRequestPolicy
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta2DeviceCapacity",)


class V1beta2DeviceCapacity(BaseModel):
    request_policy: Annotated[
        V1beta2CapacityRequestPolicy,
        BeforeValidator(_default_if_none(V1beta2CapacityRequestPolicy)),
    ] = Field(
        default_factory=lambda: V1beta2CapacityRequestPolicy(),
        serialization_alias="requestPolicy",
        validation_alias=AliasChoices("request_policy", "requestPolicy"),
        exclude_if=_exclude_if,
    )

    value: str | None = Field(default=None, exclude_if=_exclude_if)
