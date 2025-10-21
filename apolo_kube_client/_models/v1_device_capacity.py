from pydantic import AliasChoices, BaseModel, Field
from .base import _default_if_none
from .v1_capacity_request_policy import V1CapacityRequestPolicy
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1DeviceCapacity",)


class V1DeviceCapacity(BaseModel):
    request_policy: Annotated[
        V1CapacityRequestPolicy,
        BeforeValidator(_default_if_none(V1CapacityRequestPolicy)),
    ] = Field(
        default_factory=lambda: V1CapacityRequestPolicy(),
        serialization_alias="requestPolicy",
        validation_alias=AliasChoices("request_policy", "requestPolicy"),
    )

    value: str | None = None
