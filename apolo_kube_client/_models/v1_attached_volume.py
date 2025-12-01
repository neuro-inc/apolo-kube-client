from typing import Annotated, ClassVar, Final

from pydantic import Field

from .base_model import BaseConfiguredModel


__all__ = ("V1AttachedVolume",)


class V1AttachedVolume(BaseConfiguredModel):
    """AttachedVolume describes a volume attached to a node"""

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.AttachedVolume"

    device_path: Annotated[
        str,
        Field(
            alias="devicePath",
            description="""DevicePath represents the device path where the volume should be available""",
        ),
    ]

    name: Annotated[str, Field(description="""Name of the attached volume""")]
