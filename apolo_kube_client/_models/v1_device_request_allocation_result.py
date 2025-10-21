from pydantic import AliasChoices, BaseModel, Field
from .utils import _collection_if_none
from .v1_device_toleration import V1DeviceToleration
from pydantic import BeforeValidator
from typing import Annotated

__all__ = ("V1DeviceRequestAllocationResult",)


class V1DeviceRequestAllocationResult(BaseModel):
    admin_access: bool | None = Field(
        default=None,
        serialization_alias="adminAccess",
        validation_alias=AliasChoices("admin_access", "adminAccess"),
    )

    binding_conditions: Annotated[
        list[str], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="bindingConditions",
        validation_alias=AliasChoices("binding_conditions", "bindingConditions"),
    )

    binding_failure_conditions: Annotated[
        list[str], BeforeValidator(_collection_if_none("[]"))
    ] = Field(
        default=[],
        serialization_alias="bindingFailureConditions",
        validation_alias=AliasChoices(
            "binding_failure_conditions", "bindingFailureConditions"
        ),
    )

    consumed_capacity: Annotated[
        dict[str, str], BeforeValidator(_collection_if_none("{}"))
    ] = Field(
        default={},
        serialization_alias="consumedCapacity",
        validation_alias=AliasChoices("consumed_capacity", "consumedCapacity"),
    )

    device: str | None = None

    driver: str | None = None

    pool: str | None = None

    request: str | None = None

    share_id: str | None = Field(
        default=None,
        serialization_alias="shareID",
        validation_alias=AliasChoices("share_id", "shareID"),
    )

    tolerations: Annotated[
        list[V1DeviceToleration], BeforeValidator(_collection_if_none("[]"))
    ] = []
