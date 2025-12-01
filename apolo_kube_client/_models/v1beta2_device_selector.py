from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel
from .v1beta2_cel_device_selector import V1beta2CELDeviceSelector


__all__ = ("V1beta2DeviceSelector",)


class V1beta2DeviceSelector(BaseConfiguredModel):
    """DeviceSelector must have exactly one field set."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.resource.v1beta2.DeviceSelector"

    cel: Annotated[
        V1beta2CELDeviceSelector | None,
        Field(
            description="""CEL contains a CEL expression for selecting a device.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
