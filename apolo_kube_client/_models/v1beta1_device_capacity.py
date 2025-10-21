from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1beta1_capacity_request_policy import V1beta1CapacityRequestPolicy
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1beta1DeviceCapacity",)


class V1beta1DeviceCapacity(BaseModel):
    request_policy: Annotated[
        V1beta1CapacityRequestPolicy,
        BeforeValidator(_default_if_none(V1beta1CapacityRequestPolicy)),
    ] = Field(
        default_factory=lambda: V1beta1CapacityRequestPolicy(),
        serialization_alias="requestPolicy",
        validation_alias=AliasChoices("request_policy", "requestPolicy"),
    )

    value: str | None = None
