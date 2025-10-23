from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .utils import _default_if_none
from .v1_opaque_device_configuration import V1OpaqueDeviceConfiguration
from pydantic import BeforeValidator

__all__ = ("V1DeviceClassConfiguration",)


class V1DeviceClassConfiguration(BaseModel):
    """DeviceClassConfiguration is used in DeviceClass."""

    model_config = ConfigDict(validate_by_alias=True, validate_by_name=True)

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.resource.v1.DeviceClassConfiguration"
    )

    opaque: Annotated[
        V1OpaqueDeviceConfiguration | None,
        Field(
            description="""Opaque provides driver-specific configuration parameters.""",
            exclude_if=lambda v: v is None,
        ),
        BeforeValidator(_default_if_none(V1OpaqueDeviceConfiguration)),
    ] = None
