from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field


__all__ = ("V1AttachedVolume",)


class V1AttachedVolume(BaseModel):
    """AttachedVolume describes a volume attached to a node"""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.core.v1.AttachedVolume"

    device_path: Annotated[
        str,
        Field(
            alias="devicePath",
            description="""DevicePath represents the device path where the volume should be available""",
        ),
    ]

    name: Annotated[str, Field(description="""Name of the attached volume""")]
