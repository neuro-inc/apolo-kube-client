from __future__ import annotations
from pydantic import AliasChoices, BaseModel, Field
from .v1beta1_device_toleration import V1beta1DeviceToleration

__all__ = ("V1beta1DeviceRequestAllocationResult",)


class V1beta1DeviceRequestAllocationResult(BaseModel):
    admin_access: bool | None = Field(
        default=None,
        serialization_alias="adminAccess",
        validation_alias=AliasChoices("admin_access", "adminAccess"),
    )

    binding_conditions: list[str] = Field(
        default=[],
        serialization_alias="bindingConditions",
        validation_alias=AliasChoices("binding_conditions", "bindingConditions"),
    )

    binding_failure_conditions: list[str] = Field(
        default=[],
        serialization_alias="bindingFailureConditions",
        validation_alias=AliasChoices(
            "binding_failure_conditions", "bindingFailureConditions"
        ),
    )

    consumed_capacity: dict[str, str] = Field(
        default={},
        serialization_alias="consumedCapacity",
        validation_alias=AliasChoices("consumed_capacity", "consumedCapacity"),
    )

    device: str | None = Field(default=None)

    driver: str | None = Field(default=None)

    pool: str | None = Field(default=None)

    request: str | None = Field(default=None)

    share_id: str | None = Field(
        default=None,
        serialization_alias="shareID",
        validation_alias=AliasChoices("share_id", "shareID"),
    )

    tolerations: list[V1beta1DeviceToleration] = Field(default=[])
