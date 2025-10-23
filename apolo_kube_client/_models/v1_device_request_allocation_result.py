from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .utils import _exclude_if
from .v1_device_toleration import V1DeviceToleration
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1DeviceRequestAllocationResult",)


class V1DeviceRequestAllocationResult(BaseModel):
    admin_access: bool | None = Field(
        default=None,
        serialization_alias="adminAccess",
        validation_alias=AliasChoices("admin_access", "adminAccess"),
        exclude_if=_exclude_if,
    )

    binding_conditions: Annotated[
        list[str], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="bindingConditions",
        validation_alias=AliasChoices("binding_conditions", "bindingConditions"),
        exclude_if=_exclude_if,
    )

    binding_failure_conditions: Annotated[
        list[str], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="bindingFailureConditions",
        validation_alias=AliasChoices(
            "binding_failure_conditions", "bindingFailureConditions"
        ),
        exclude_if=_exclude_if,
    )

    consumed_capacity: Annotated[
        dict[str, str], BeforeValidator(_collection_if_none("{}"))
    ] = Field(
        default={},
        serialization_alias="consumedCapacity",
        validation_alias=AliasChoices("consumed_capacity", "consumedCapacity"),
        exclude_if=_exclude_if,
    )

    device: str | None = Field(default=None, exclude_if=_exclude_if)

    driver: str | None = Field(default=None, exclude_if=_exclude_if)

    pool: str | None = Field(default=None, exclude_if=_exclude_if)

    request: str | None = Field(default=None, exclude_if=_exclude_if)

    share_id: str | None = Field(
        default=None,
        serialization_alias="shareID",
        validation_alias=AliasChoices("share_id", "shareID"),
        exclude_if=_exclude_if,
    )

    tolerations: Annotated[
        list[V1DeviceToleration], BeforeValidator(_collection_if_none("[]"))
    ] = Field(default=[], exclude_if=_exclude_if)
