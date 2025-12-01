from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel
from .v1beta2_opaque_device_configuration import V1beta2OpaqueDeviceConfiguration


__all__ = ("V1beta2DeviceClassConfiguration",)


class V1beta2DeviceClassConfiguration(BaseConfiguredModel):
    """DeviceClassConfiguration is used in DeviceClass."""

    kubernetes_ref: ClassVar[Final[str]] = (
        "io.k8s.api.resource.v1beta2.DeviceClassConfiguration"
    )

    opaque: Annotated[
        V1beta2OpaqueDeviceConfiguration | None,
        Field(
            description="""Opaque provides driver-specific configuration parameters.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
