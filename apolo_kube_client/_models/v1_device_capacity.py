from pydantic import AliasChoices, BaseModel, Field
from .v1_capacity_request_policy import V1CapacityRequestPolicy

__all__ = ("V1DeviceCapacity",)


class V1DeviceCapacity(BaseModel):
    request_policy: V1CapacityRequestPolicy = Field(
        default_factory=lambda: V1CapacityRequestPolicy(),
        serialization_alias="requestPolicy",
        validation_alias=AliasChoices("request_policy", "requestPolicy"),
    )

    value: str | None = None
