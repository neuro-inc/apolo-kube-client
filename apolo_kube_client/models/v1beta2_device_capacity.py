from pydantic import AliasChoices, BaseModel, Field
from .v1beta2_capacity_request_policy import V1beta2CapacityRequestPolicy

__all__ = ("V1beta2DeviceCapacity",)


class V1beta2DeviceCapacity(BaseModel):
    request_policy: V1beta2CapacityRequestPolicy = Field(
        default_factory=lambda: V1beta2CapacityRequestPolicy(),
        serialization_alias="requestPolicy",
        validation_alias=AliasChoices("request_policy", "requestPolicy"),
    )

    value: str | None = None
