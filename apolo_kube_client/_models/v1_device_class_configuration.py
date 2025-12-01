from typing import Annotated, ClassVar, Final

from pydantic import BaseModel, Field

from .v1_opaque_device_configuration import V1OpaqueDeviceConfiguration


__all__ = ("V1DeviceClassConfiguration",)


class V1DeviceClassConfiguration(BaseModel):
    """DeviceClassConfiguration is used in DeviceClass."""

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.resource.v1.DeviceClassConfiguration"
    )

    opaque: Annotated[
        V1OpaqueDeviceConfiguration | None,
        Field(
            description="""Opaque provides driver-specific configuration parameters.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
