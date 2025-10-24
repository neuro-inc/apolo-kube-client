from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1beta2_opaque_device_configuration import V1beta2OpaqueDeviceConfiguration
from pydantic import BeforeValidator

__all__ = ("V1beta2DeviceClassConfiguration",)


class V1beta2DeviceClassConfiguration(BaseModel):
    """DeviceClassConfiguration is used in DeviceClass."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.resource.v1beta2.DeviceClassConfiguration"
    )

    opaque: Annotated[
        V1beta2OpaqueDeviceConfiguration | None,
        Field(
            description="""Opaque provides driver-specific configuration parameters.""",
            exclude_if=lambda v: v is None,
        ),
        BeforeValidator(_default_if_none(V1beta2OpaqueDeviceConfiguration)),
    ] = None
