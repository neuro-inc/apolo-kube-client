from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1VolumeDevice",)


class V1VolumeDevice(BaseConfiguredModel):
    """volumeDevice describes a mapping of a raw block device within a container."""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.VolumeDevice"

    device_path: Annotated[
        str,
        Field(
            alias="devicePath",
            description="""devicePath is the path inside of the container that the device will be mapped to.""",
        ),
    ]

    name: Annotated[
        str,
        Field(
            description="""name must match the name of a persistentVolumeClaim in the pod"""
        ),
    ]
