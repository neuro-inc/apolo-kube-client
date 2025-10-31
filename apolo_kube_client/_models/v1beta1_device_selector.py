from typing import Annotated, ClassVar, Final
from pydantic import BaseModel, ConfigDict, Field
from .v1beta1_cel_device_selector import V1beta1CELDeviceSelector

__all__ = ("V1beta1DeviceSelector",)


class V1beta1DeviceSelector(BaseModel):
    """DeviceSelector must have exactly one field set."""

    model_config = ConfigDict(
        extra="forbid",
        serialize_by_alias=True,
        validate_by_alias=True,
        validate_by_name=True,
    )

    kubernetes_ref: ClassVar[Final[str]] = "io.k8s.api.resource.v1beta1.DeviceSelector"

    cel: Annotated[
        V1beta1CELDeviceSelector | None,
        Field(
            description="""CEL contains a CEL expression for selecting a device.""",
            exclude_if=lambda v: v is None,
        ),
    ] = None
