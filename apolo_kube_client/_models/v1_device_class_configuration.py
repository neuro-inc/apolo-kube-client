from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel
from .v1_opaque_device_configuration import V1OpaqueDeviceConfiguration


__all__ = ("V1DeviceClassConfiguration",)


class V1DeviceClassConfiguration(BaseConfiguredModel):
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
